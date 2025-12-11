import os
import sys
import json
import argparse
from typing import List, Dict, Any
from termcolor import cprint
from jenkins import Jenkins, JenkinsException
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


JENKINS_URL_ENV = 'JENKINS_URL'
JENKINS_USER_ENV = 'JENKINS_USER'
JENKINS_TOKEN_ENV = 'JENKINS_TOKEN'


def get_installed_plugins(server: Jenkins) -> List[Dict[str, Any]]:
    plugins_list = server.get_plugins()
    cprint(f"\n--- Found {len(plugins_list)} Plugins ---", "blue")

    simple_plugins = []
    for plugin in plugins_list.values():
        simple_plugins.append({
            'name': plugin.get('longName', plugin.get('shortName')),
            'version': plugin.get('version'),
            'active': plugin.get('active', False)
        })
    return simple_plugins


def get_shared_libraries(server: Jenkins) -> List[Dict[str, Any]]:

    groovy_script = """
    import org.jenkinsci.plugins.workflow.libs.GlobalLibraries
    import groovy.json.JsonBuilder

    // Check if the class exists (plugin installed) to avoid script errors
    try {
        Class.forName("org.jenkinsci.plugins.workflow.libs.GlobalLibraries")
    } catch (ClassNotFoundException e) {
        print "[]"
        return
    }

    def libs = GlobalLibraries.get().getLibraries().collect { lib ->
        // Handle different retriever types (modern vs legacy)
        def retrieverDesc = "Unknown"
        def scmUrl = "N/A"
        
        // DEBUGGING MODE: aggressive inspection
        try {
            if (lib.retriever) {
                 retrieverDesc = lib.retriever.class.name
                 
                 // modern SCM retriever
                 if (lib.retriever.hasProperty('scm')) {
                     def scm = lib.retriever.scm
                     retrieverDesc += " -> SCM: " + scm.class.name
                     
                     // 1. Try 'remote' (Git Branch Source / SCMSource) - FOUND IN DEBUG
                     if (scm.hasProperty('remote')) {
                         scmUrl = scm.remote
                     }
                     // 2. Try 'userRemoteConfigs' (Standard GitSCM)
                     else if (scm.hasProperty('userRemoteConfigs')) {
                        def configs = scm.userRemoteConfigs
                        if (configs && configs.size() > 0) {
                            scmUrl = configs[0].url
                        }
                     } 
                     // 3. Fallback
                     else {
                         scmUrl = "Unknown SCM properties: " + scm.properties.keySet().toString()
                     }
                 } 
                 // Legacy or different retriever type
                 else {
                     scmUrl = "Retriever props: " + lib.retriever.properties.keySet().toString()
                 }
            }
        } catch (Exception e) {
            scmUrl = "Error: " + e.toString()
        }
        
        [
            name: lib.name,
            defaultVersion: lib.defaultVersion,
            implicit: lib.implicit,
            allowVersionOverride: lib.allowVersionOverride,
            retriever: retrieverDesc,
            url: scmUrl
        ]
    }
    println new JsonBuilder(libs).toString()
    """
    
    try:

        response_text = server.run_script(groovy_script)
        if not response_text:
             return []
             
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']')
        
        if start_idx == -1 or end_idx == -1:
             cprint(f"Warning: No valid JSON found in response: {response_text[:100]}...", "yellow")
             return []
             
        clean_json = response_text[start_idx:end_idx+1]
        
        libraries = json.loads(clean_json)
        cprint(f"\n--- Found {len(libraries)} Shared Libraries ---", "blue")
        return libraries
    except Exception as e:
        cprint(f"Warning: Failed to retrieve shared libraries: {e}", "yellow")
        return []



def get_all_jobs(server: Jenkins) -> List[Dict[str, Any]]:
    jobs_list = server.get_all_jobs()
    cprint(f"\n--- Found {len(jobs_list)} Jobs ---", "blue")
    return jobs_list


def main():
    jenkins_url = os.getenv(JENKINS_URL_ENV)
    username = os.getenv(JENKINS_USER_ENV)
    token = os.getenv(JENKINS_TOKEN_ENV)
    if not jenkins_url or not username or not token:
        cprint("\nFATAL: Missing required environment variables.", "red")
        cprint("Please set: JENKINS_URL, JENKINS_USER, and JENKINS_TOKEN", "yellow")
        print("-" * 50)
        sys.exit(1)

    try:
        cur_server = Jenkins(jenkins_url, username=username, password=token)
        # server.get_version()
        # cprint("Connection successful.", "green")
    except JenkinsException as e:
        cprint(f"❌ Error connecting to Jenkins or during API call: {e}", "red")
        sys.exit(1)

    plugins = get_installed_plugins(cur_server)
    jobs = get_all_jobs(cur_server)
    shared_libs = get_shared_libraries(cur_server)

    if plugins:
        print("-" * 80)
        for p in plugins:
            status = " [ACTIVE]" if p['active'] else " [INACTIVE]"
            print(f"Plugin: {p['name']:40} | Version: {p['version']:10} | Status: {status}")
        print("-" * 80)

    if shared_libs:
        print("-" * 80)
        for lib in shared_libs:
            # Handle potential None values safely
            name = lib.get('name', 'Unknown')
            ver = lib.get('defaultVersion') or 'N/A'
            implicit = lib.get('implicit', False)
            retriever = lib.get('retriever', 'Unknown')
            url = lib.get('url', 'N/A')
            
            print(f"Library: {name:20} | Ver: {ver:10} | Implicit: {str(implicit):5} | URL: {url}")
        print("-" * 80)

    if jobs:
        print("-" * 80)
        for job in jobs:
            print(f"Job: {job['name']:50} | URL: {job['url']}")
        print("=" * 80)


if __name__ == "__main__":
    main()
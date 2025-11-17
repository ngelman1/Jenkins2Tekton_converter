import os
import sys
import argparse
from typing import List, Dict, Any
from termcolor import cprint
from jenkins import Jenkins, JenkinsException
from dotenv import load_dotenv
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



def get_all_jobs(server: Jenkins) -> List[Dict[str, Any]]:
    jobs_list = server.get_all_jobs()
    cprint(f"\n--- Found {len(jobs_list)} Jobs ---", "blue")
    return jobs_list


def main():
    load_dotenv()
    jenkins_url = os.getenv(JENKINS_URL_ENV)
    username = os.getenv(JENKINS_USER_ENV)
    token = os.getenv(JENKINS_TOKEN_ENV)
    if not jenkins_url or not username or not token:
        cprint("\nFATAL: Missing critical env var. Ensure ENKINS_URL, JENKINS_USER, and JENKINS_TOKEN are defined in your .env file ", "red")
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

    if plugins:
        print("-" * 80)
        for p in plugins:
            status = " [ACTIVE]" if p['active'] else " [INACTIVE]"
            print(f"Plugin: {p['name']:40} | Version: {p['version']:10} | Status: {status}")
        print("-" * 80)
    if jobs:
        print("-" * 80)
        for job in jobs:
            print(f"Job: {job['name']:50} | URL: {job['url']}")
        print("=" * 80)


if __name__ == "__main__":
    main()
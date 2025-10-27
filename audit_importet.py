import os
import sys
import subprocess
import json
import time
from pathlib import Path
from termcolor import cprint
from typing import Dict, Any

def read_jenkinsfile(filename:str) -> str:
    if not Path(filename).exists():
        cprint(f"File -'{filename}' does not exist in this directry" , "red")
        exit(1)

    with open(filename , 'r' , encoding='utf-8') as file:
        return file.read()
    


def execute_cli_command(jenkinsfile_path: Path, output_dir: Path) -> subprocess.CompletedProcess:
    cprint(f"Executing CLI audit for: {jenkinsfile_path.name}", "yellow")
    
    command = [
        "actions-importer", 
        "audit", 
        "jenkins", 
        f"--jenkinsfile-path={jenkinsfile_path}", 
        f"--output-dir={output_dir}"
    ]
    
    # Run the command and capture output. check=True raises CalledProcessError on failure.
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    cprint("CLI command executed successfully.", "green")
    
    return result


def parse_audit_output(output_dir: Path) -> str:
    """Reads the audit.json file from the temp directory and returns its content."""
    
    audit_file_path = output_dir / "audit.json"
    
    if not audit_file_path.exists():
        cprint("Error: audit.json not found in temporary output.", "red")
        return "Audit failed: Output file missing."

    with open(audit_file_path, 'r') as f:
        audit_data = json.load(f)
        
    # Return the entire JSON object as a formatted string
    return json.dumps(audit_data, indent=2)



def get_jenkins_audit(jenkinsfile_name: str) -> str:
    """
    Orchestrator function: Runs the GitHub Actions Importer audit tool,
    cleans up temporary files, and returns the structured audit JSON.
    """
    
    jenkinsfile_path = Path(jenkinsfile_name).resolve() # Get absolute path for the CLI
    output_dir = "" # Initialize outside try block

    try:
        read_jenkinsfile(jenkinsfile_path) 
        result, output_dir = execute_cli_command(jenkinsfile_path)
        audit_json_string = parse_audit_output(output_dir)
        
        cprint("Audit successfully completed and JSON retrieved.", "green")
        return audit_json_string

    except subprocess.CalledProcessError as e:
        cprint(f"Error: CLI execution failed. Stderr: {e.stderr}", "red")
        return f"Audit failed: CLI execution error. Stderr: {e.stderr}"
    
    except Exception as e:
        cprint(f"An unexpected error occurred during audit: {e}", "red")
        return f"Audit failed: {e}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run GitHub Actions Importer Audit on a Jenkinsfile.')
    parser.add_argument('jenkinsfile_name', help='Name of the Jenkinsfile in the current directory.')
    args = parser.parse_args()
    
    audit_result = get_jenkins_audit(args.jenkinsfile_name)
    cprint("\n--- FINAL AUDIT RESULT (for prompt) ---", "blue")
    print(audit_result)
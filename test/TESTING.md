## Test Case: Checking Docker is installed ✅

### 📂 File Location
Input File: test/Jenkinsfile_Lib1

### The Jenkinsfile Logic
1. isDockerAvailable(): Calls the shared library step.

2. boolean dockerExists: Captures the true or false result.

3. if (dockerExists): Uses standard Groovy logic to decide whether to print a success message or fail the build with an error.

expected output is either "Docker is available" or "Docker is missing."




## Test Case: Jenkinsfile_Lib1 (Shared Library Git Setup) ❌
This test case validates the conversion of a Jenkins Pipeline that utilizes an external Shared Library to perform a specific utility task: configuring Git identity.

It is designed to verify that the Jenkins2Tekton converter can correctly identify, isolate, and translate custom library steps (gitSetup) into functional Tekton Tasks.

### 📂 File Location
Input File: test/Jenkinsfile_Lib2

Library Used: HariSekhon/Jenkins (specifically vars/gitSetup.groovy)


### The Jenkinsfile Logic
The Jenkinsfile_Lib1 defines a simple pipeline with three stages:

1. Initialize: Prints a start message.

2. Basic Git Setup: Calls the custom Shared Library step gitSetup("Setting up global Git identity").

This step looks for an env vars called: $GIT_USERNAME , $GIT_EMAIL.
if not found, there are set to be $GIT_USERNAME = Jenkins , $GIT_EMAIL = jenkins@noreply.

3. Verify Setup: Runs git config --get commands to prove the identity was set correctly

To faithfully replicate the logic of vars/gitSetup.groovy, the generated git-setup Task must not simply rely on static defaults. It must implement the same fallback logic as the original code.

**currently fails- assigns the default values "Tekton CI" and "tekton-ci@example.com" without checking for real env vars
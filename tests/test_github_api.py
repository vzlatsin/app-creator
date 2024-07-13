import os
import sys
import json

# Add the src directory to the system path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now we can import GitHubAPI from the src directory
from github_api import GitHubAPI

# Load configuration from config.json
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path) as config_file:
    config = json.load(config_file)

def main():
    # Retrieve the GitHub token from the configuration file
    github_token = config.get('GITHUB_TOKEN')

    # Check if the token is set
    if not github_token:
        print("Please set the GITHUB_TOKEN in the config.json file.")
        return

    # Create an instance of the GitHubAPI class
    github_api = GitHubAPI(github_token)

    # Define the name of the repository to be created
    repo_name = "test-repo"

    # Call the create_repo method to create the repository
    result = github_api.create_repo(repo_name)

    # Print the result
    if result:
        print("Repository created successfully.")
    else:
        print("Failed to create repository.")

if __name__ == "__main__":
    main()

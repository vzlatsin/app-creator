import requests  # Importing the requests library to make HTTP requests

class GitHubAPI:
    def __init__(self, token):
        # Initialize the GitHub API with the provided token
        # The token is used for authenticating requests to the GitHub API
        self.token = token
        # Setting up the headers for the requests
        self.headers = {
            'Authorization': f'token {self.token}',  # Authorization header with the token
            'Accept': 'application/vnd.github.v3+json'  # Accept header specifying the GitHub API version
        }

    def create_repo(self, repo_name):
        # URL for creating a new GitHub repository
        url = 'https://api.github.com/user/repos'
        # Data payload for the request
        data = {
            'name': repo_name,  # Name of the repository to be created
            'private': False  # Set to True if you want a private repo, False for a public repo
        }
        # Make the POST request to GitHub API
        response = requests.post(url, headers=self.headers, json=data)
        # Check if the repository was created successfully
        if response.status_code == 201:
            print(f'Repository {repo_name} created successfully.')
            return response.json()  # Return the response JSON if successful
        else:
            print(f'Error creating repository: {response.json()}')
            return None  # Return None if there was an error
 

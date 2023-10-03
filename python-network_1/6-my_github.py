import requests
import sys

# Check if username and personal access token arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

# Define the GitHub API endpoint to get user information
url = "https://api.github.com/user"

# Set up the Basic Authentication header using your personal access token
headers = {
    "Authorization": f"Basic {username}:{personal_access_token}"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        if user_id:
            print(f"Your GitHub user ID is: {user_id}")
        else:
            print("Unable to fetch user ID from the response.")
    else:
        print(
            f"Failed to fetch user information. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

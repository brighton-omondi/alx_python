import requests
import sys

# Checks if both URL and email address arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Creates a dictionary with the email parameter
data = {'email': email}

try:
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Your email is:", email)
        print(response.text)
    else:
        print(
            f"Failed to send POST request to {url}. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

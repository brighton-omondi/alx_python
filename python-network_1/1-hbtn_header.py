import requests
import sys

# Checks if a URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
    else:
        print(
            f"Failed to fetch data from {url}. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

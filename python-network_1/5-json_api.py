import requests
import sys

# Checks if an argument (letter) is provided
if len(sys.argv) != 2:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {"q": q}

try:
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

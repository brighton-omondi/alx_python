import requests
import json
import sys

def get_employee_data(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee data
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Fetch TODO list data
    response = requests.get(todos_url)
    todos_data = response.json()

    return user_id, username, todos_data

def export_to_json(employee_id):
    user_id, username, todos_data = get_employee_data(employee_id)

    json_filename = f"{user_id}.json"

    data_to_export = {str(user_id): [{"task": todo["title"], "completed": todo["completed"], "username": username} for todo in todos_data]}

    with open(json_filename, mode='w') as json_file:
        json.dump(data_to_export, json_file, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        export_to_json(employee_id)
        print(f"Data has been exported to {employee_id}.json")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    # Fetch the user data and tasks data
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if users_response.status_code != 200 or tasks_response.status_code != 200:
        print("Failed to fetch data.")
        sys.exit(1)

    users = users_response.json()
    tasks = tasks_response.json()

    # Create a dictionary to store the tasks for each user
    user_tasks = {}

    # Populate the user_tasks dictionary
    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_tasks[user_id] = []

        for task in tasks:
            if task["userId"] == user_id:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                user_tasks[user_id].append(task_data)

    # Write the data to the output file in JSON format
    with open(output_file, "w") as json_file:
        json.dump(user_tasks, json_file)

    print(f"Data exported to {output_file}")

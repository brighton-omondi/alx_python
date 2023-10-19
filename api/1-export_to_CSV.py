import requests
import sys
import csv

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

    # Create a list of tasks in the required format
    tasks = []
    for todo in todos_data:
        task_completed = todo["completed"]
        task_title = todo["title"]
        tasks.append([str(user_id), username, str(task_completed), task_title])

    return user_id, username, tasks

def export_to_csv(user_id, username, tasks):
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write the tasks
        csvwriter.writerows(tasks)
    print(f"Data has been exported to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        user_id, username, tasks = get_employee_data(employee_id)
        if tasks:
            export_to_csv(user_id, username, tasks)
        else:
            print(f"No tasks found for employee with ID {employee_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
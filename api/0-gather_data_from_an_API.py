import requests

def get_employee_todo_list_progress(employee_id):
    """Gets the employee TODO list progress for the given employee ID.

    Args:
        employee_id: The employee ID.

    Returns:
        A dictionary containing the employee TODO list progress, with the following keys:
            "name": The employee name.
            "done_tasks": The number of completed tasks.
            "total_tasks": The total number of tasks.
    """

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(url)
    response_json = response.json()

    done_tasks = 0
    total_tasks = 0
    for todo in response_json:
        if todo["completed"]:
            done_tasks += 1
        total_tasks += 1

    return {
        "name": response_json[0]["name"],
        "done_tasks": done_tasks,
        "total_tasks": total_tasks,
    }

def print_employee_todo_list_progress(employee_todo_list_progress):
    """Prints the employee TODO list progress in the specified format.

    Args:
        employee_todo_list_progress: A dictionary containing the employee TODO list progress, with the following keys:
            "name": The employee name.
            "done_tasks": The number of completed tasks.
            "total_tasks": The total number of tasks.
    """

    print("Employee {} is done with tasks({}/{}):".format(
        employee_todo_list_progress["name"],
        employee_todo_list_progress["done_tasks"],
        employee_todo_list_progress["total_tasks"],
    ))

    for todo in employee_todo_list_progress["todos"]:
        print("\t{}".format(todo["title"]))

def main():
    employee_id = int(input("Enter the employee ID: "))

    employee_todo_list_progress = get_employee_todo_list_progress(employee_id)
    print_employee_todo_list_progress(employee_todo_list_progress)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys
import requests

def get_employee_todo_progress(employee_id):
    # Define the base URL
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee information
    employee_url = f'{base_url}/users/{employee_id}'
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        return

    employee = response.json()
    employee_name = employee['name']

    # Fetch employee's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee ID {employee_id}")
        return

    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
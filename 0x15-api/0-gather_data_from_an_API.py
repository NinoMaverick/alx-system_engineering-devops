#!/usr/bin/python3
<<<<<<< HEAD
"""script returning info on employee TODO list"""
=======
"""For a given employee ID, returns information about
their TODO list progress"""
>>>>>>> e5d60066986b5a820a4b97e1188c17a5239ce4fe

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
<<<<<<< HEAD
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
=======

    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()

    params = {"userId": employee_id}
    
    todos_response = requests.get(url + 'todos', params=params)
    
    todos = todos_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks ({}/{})".format(user.get("name"),
                                                          len(completed), len(todos)))
    
    for complete in completed:
        print("\t {}".format(complete))
>>>>>>> e5d60066986b5a820a4b97e1188c17a5239ce4fe

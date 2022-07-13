#!/usr/bin/python3
"""Get todos from user."""
import requests
from sys import argv

          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    todos = todos.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    finished = []
    for todo in todos:
        if todo.get('completed'):
            finished.append(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(finished), len(todos)))
    for todo in finished:
        print("\t {}".format(todo.get('title')))

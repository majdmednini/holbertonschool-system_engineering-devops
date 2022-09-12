#!/usr/bin/python3
"""
returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

    completed = 0
    total = 0
    completed_tasks = []

    for task in todo:
        total_nb += 1
        if task.get("completed") is True:
            completed += 1
            completed_tasks.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
    print(sentence.format(user.get("name"), completed, total_nb))
    for task in completed_tasks:
        print("\t {}".format(task))

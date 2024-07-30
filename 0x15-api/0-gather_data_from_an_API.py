#!/usr/bin/python3
"""
This module uses a REST API for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
import sys


if __name__ == "__main__":

    url_1 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    response_1 = requests.get(url_1)
    users = response_1.json()
    EMPLOYEE_NAME = users.get("name")

    url_2 = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userID': sys.argv[1]}
    response_2 = requests.get(url_2, params=params)
    todos = response_2.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for i in todos:
        if isinstance(i, dict):
            TOTAL_NUMBER_OF_TASKS += 1
        if i.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(i.get("title"))
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for i in TASK_TITLE:
        print("\t " + i)

#!/usr/bin/python3
"""
Exporting data in JSON format
"""


import json
import requests
import sys


def main():
    USER_ID = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    response_user = requests.get(url_user)
    users = response_user.json()
    USERNAME = users.get("username")
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': USER_ID}
    response = requests.get(url_todos, params=params)

    if response.status_code == 200:
        todos = response.json()

    todos_list = []
    for i in todos:
        COMPLETED = i.get("completed")
        TASK = i.get("title")
        users_dict = {"task": TASK, "completed": COMPLETED,
                      "username": USERNAME}
        todos_list.append(users_dict)

    todos_dict = {USER_ID: todos_list}
    filename = f"{USER_ID}.json"
    with open(filename, 'w') as f:
        json.dump(todos_dict, f)


if __name__ == "__main__":
    main()

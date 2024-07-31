#!/usr/bin/python3
"""
Exporting data in JSON format
"""


import json
import requests
import sys


def main():
    url_users = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(url_users)
    users = users_response.json()

    if users_response.status_code == 200:
        new_dict = {}
        for user in users:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            url_todos = 'https://jsonplaceholder.typicode.com/todos'
            params = {'userId': USER_ID}
            response_todos = requests.get(url_todos, params=params)
            if response_todos.status_code == 200:
                todos = response_todos.json()
                todos_list = []
                for i in todos:
                    COMPLETED = i.get("completed")
                    TASK = i.get("title")
                    users_dict = {
                            "username": USERNAME,
                            "task": TASK,
                            "completed": COMPLETED}
                    todos_list.append(users_dict)
                    new_dict[USER_ID] = todos_list

    with open('todo_all_employees.json', 'w', newline='') as f:
        json.dump(new_dict, f)


if __name__ == "__main__":
    main()

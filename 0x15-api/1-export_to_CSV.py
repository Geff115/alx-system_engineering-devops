#!/usr/bin/python3
"""
Exporting data in CSV format
"""


import csv
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

    # filename will be gotten from the command line
    filename = f"{USER_ID}.csv"
    with open(filename, 'w', newline='') as f:
        write_csv = csv.DictWriter(f, fieldnames=["USER_ID", "USERNAME",
                                   "TASK_COMPLETED_STATUS", "TASK_TITLE"],
                                   quotechar='"', quoting=csv.QUOTE_ALL)

        for i in todos:
            TASK_COMPLETED_STATUS = i.get("completed")
            TASK_TITLE = i.get("title")
            row = {
                "USER_ID": USER_ID,
                "USERNAME": USERNAME,
                "TASK_COMPLETED_STATUS": TASK_COMPLETED_STATUS,
                "TASK_TITLE": TASK_TITLE
            }
            write_csv.writerow(row)


if __name__ == "__main__":
    main()

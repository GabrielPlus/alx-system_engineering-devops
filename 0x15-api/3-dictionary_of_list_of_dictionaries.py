#!/usr/bin/python3
<<<<<<< HEAD
"""
    Uses the fake API to get all employers and their todos and export as json
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_employ = "https://jsonplaceholder.typicode.com/users"
    r_employs = requests.get(url_employ).json()
    report = {}
    for employ in r_employs:
        id_em = employ.get("id")
        url_todos = url_employ + "/{}/todos".format(id_em)
        r_todos = requests.get(url_todos).json()
        username = employ.get("username")
        total_num_task = r_todos
        list_dict_report = []
        for task in total_num_task:
            id_report = {}
            id_report["username"] = str(username)
            id_report["completed"] = task.get("completed")
            id_report["task"] = str(task.get("title"))
            list_dict_report.append(id_report)
        report[id_em] = list_dict_report
    with open("todo_all_employees.json", "w") as fjson:
        fjson.write(json.dumps(report))
=======
"""Python script to export data in the JSON format"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''
    response = requests.get(base_url + 'users/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    users = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    data = {}
    for user in users:
        user_todos = [todo for todo in todos
                      if todo.get('userId') == user.get('id')]
        user_todos = [{'username': user.get('username'),
                       'task': todo.get('title'),
                       'completed': todo.get('completed')}
                      for todo in user_todos]
        data[str(user.get('id'))] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    do_request()
>>>>>>> 5af6ec72da8ea87e9faa22c74fd05b9bea8e2dc6

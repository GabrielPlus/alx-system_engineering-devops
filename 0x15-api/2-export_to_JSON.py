#!/usr/bin/python3
<<<<<<< HEAD
"""
    Uses the fake API to get an employer and export the info in json formater
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    id_em = argv[1]
    url_employ = "https://jsonplaceholder.typicode.com/users/{}".format(id_em)
    url_todos = url_employ + "/todos"
    r_employ = requests.get(url_employ).json()
    r_todos = requests.get(url_todos).json()
    username = r_employ.get("username")
    total_num_task = r_todos
    list_dict_report = []
    for task in total_num_task:
        id_report = {}
        id_report["username"] = str(username)
        id_report["completed"] = task.get("completed")
        id_report["task"] = str(task.get("title"))
        list_dict_report.append(id_report)
    report = {}
    report[id_em] = list_dict_report
    with open("{}.json".format(id_em), "w") as fjson:
        fjson.write(json.dumps(report))
=======
"""Python script to export data in the JSON format"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''

    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()
    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]

    user_todos = [{'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': user.get('username')}
                  for todo in user_todos]
    data = {eid: user_todos}
    with open(eid + '.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    do_request()
>>>>>>> 5af6ec72da8ea87e9faa22c74fd05b9bea8e2dc6

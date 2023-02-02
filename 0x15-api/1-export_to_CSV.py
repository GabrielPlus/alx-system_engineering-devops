#!/usr/bin/python3
<<<<<<< HEAD
"""
    Uses the fake API to get an employer and export the info in csv formater
"""
import csv
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
    list_report = []
    for task in total_num_task:
        report = {}
        report["USER_ID"] = str(task.get("userId"))
        report["USERNAME"] = str(username)
        report["TASK_COMPLETED_STATUS"] = str(task.get("completed"))
        report["TASK_TITLE"] = str(task.get("title"))
        list_report.append(report)
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open("{}.csv".format(id_em), "w") as fcsv:
        f_csv = csv.DictWriter(fcsv, fieldnames=header, quoting=csv.QUOTE_ALL)
        f_csv.writerows(list_report)
=======
"""Python script to export data in the CSV format"""

import csv
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''

    if not len(sys.argv):
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

    with open(eid + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n',
                            quoting=csv.QUOTE_ALL)
        [writer.writerow(['{}'.format(field) for field in
                          (todo.get('userId'), user.get('username'),
                           todo.get('completed'), todo.get('title'))])
         for todo in user_todos]


if __name__ == '__main__':
    do_request()
>>>>>>> 5af6ec72da8ea87e9faa22c74fd05b9bea8e2dc6

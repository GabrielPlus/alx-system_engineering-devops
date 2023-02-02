#!/usr/bin/python3
"""
<<<<<<< HEAD
    Uses the fake API to get an employer
"""
import requests
from sys import argv

if __name__ == "__main__":
    id_em = argv[1]
    url_employ = "https://jsonplaceholder.typicode.com/users/{}".format(id_em)
    url_todos = url_employ + "/todos"
    r_employ = requests.get(url_employ).json()
    r_todos = requests.get(url_todos).json()
    name = r_employ.get("name")
    total_num_task = r_todos
    done_task = [task for task in r_todos if task.get("completed")]
    output = "Employee {} is done with tasks({}/{}):".format(
                name, len(done_task), len(total_num_task))
    for task in done_task:
        output += "\n\t " + task.get("title")
    print(output)
=======
    Given employee ID, returns information about his/her TODO list progress.
"""


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
    print('Employee', user.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]


if __name__ == '__main__':
    do_request()
>>>>>>> 5af6ec72da8ea87e9faa22c74fd05b9bea8e2dc6

#!/usr/bin/python3
"""
Python script that, using the JSON PLACEHOLDER API,
for a given employee ID, export data in the CSV format.
"""
import requests
import sys


def export_to_csv(uid):
    """
    Gets data from JSON PLACEHOLDER API and writes into csv format
    Args:
        uid: employee id
    Return:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    userTodos = requests.get(base + "todos", params={"userId": uid}).json()
    with open("{}.csv".format(uid), 'w', encoding="utf-8") as w:
        for _ in userTodos:
            row = '"{}","{}","{}","{}"\n'.format(
                uid, user.get("username"), _.get("completed"), _.get("title"))
            w.write(row)


if __name__ == "__main__":
    export_to_csv(sys.argv[1])

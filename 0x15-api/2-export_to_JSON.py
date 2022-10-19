#!/usr/bin/python3
"""
Python script that, using the JSON PLACEHOLDER API,
for a given employee ID, export data in the JSON format.
"""
import json
import requests
import sys


def export_to_json(uid):
    """
    Gets data from JSON PLACEHOLDER API and writes into json format
    Args:
        uid: employee id
    Return:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    userTodos = requests.get(base + "todos", params={"userId": uid}).json()
    with open("{}.json".format(uid), 'w', encoding="utf-8") as w:
        data = {uid: []}
        for _ in userTodos:
            row = {"task": _.get("title"), "completed": _.get("completed"),
                   "username": user.get("username")}
            data[uid].append(row)
        w.write(json.dumps(data))


if __name__ == "__main__":
    export_to_json(sys.argv[1])

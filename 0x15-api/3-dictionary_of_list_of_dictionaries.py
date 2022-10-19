#!/usr/bin/python3
"""
Python script that, using the JSON PLACEHOLDER API,
for all employees, export data in the JSON format.
"""
import json
import requests


def export_all_to_json():
    """
    Gets data from JSON PLACEHOLDER API and writes into json format
    Return:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base + "users").json()
    data = {}
    for user in users:
        _data = []
        userTodos = requests.get(
            base + "todos", params={"userId": user["id"]}).json()
        for _ in userTodos:
            row = {"username": user.get("username"),
                   "task": _.get("title"), "completed": _.get("completed")}
            _data.append(row)
        data.update({user["id"]: _data})
    with open("todo_all_employees.json", 'w', encoding="utf-8") as w:
        w.write(json.dumps(data))


if __name__ == "__main__":
    export_all_to_json()

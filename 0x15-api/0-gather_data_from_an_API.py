#!/usr/bin/python3
"""
Python script that, using the JSON PLACEHOLDER API,
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


def get_data_from_api(uid):
    """
    Gets and prints data from JSON PLACEHOLDER API
    Args:
        uid: employee id
    Return:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    userTodos = requests.get(base + "todos", params={"userId": uid}).json()
    completed = [_.get("title") for _ in userTodos if _.get("completed")]
    output = "Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(userTodos))
    print("\n\t ".join([output] + completed))


if __name__ == "__main__":
    get_data_from_api(sys.argv[1])

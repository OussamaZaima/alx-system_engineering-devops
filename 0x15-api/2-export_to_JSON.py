#!/usr/bin/python3
"""Export in a json format the to-do list of an employee with a given ID."""
import json
import requests
import sys

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com"
    userId = sys.argv[1]

    # Fetch user information first
    eUrl = f"{baseUrl}/users/{userId}"
    eRes = requests.get(eUrl).json()

    # Fetch the todos with the user information
    tUrl = f"{baseUrl}/todos"
    tRes = requests.get(tUrl, params={"userId": userId}).json()

    username = eRes.get("username")
    tasks = [{"task": t.get("title"), "completed": t.get("completed"),
              "username": username} for t in tRes]
    data = {userId: tasks}

    with open(f"{userId}.json", "w") as jfile:
        json.dump(data, jfile)

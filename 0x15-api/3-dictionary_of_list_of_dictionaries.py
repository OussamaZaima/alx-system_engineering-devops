#!/usr/bin/python3
"""Export in a json format the to-do list of all employees."""
import json
import requests
import sys

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com"

    # Fetch user information first
    eUrl = f"{baseUrl}/users"
    eRes = requests.get(eUrl).json()

    # Fetch the todos with the user information
    data = {}
    for user in eRes:
        userId = user.get("id")
        username = user.get("username")
        tUrl = f"{baseUrl}/todos"
        tRes = requests.get(tUrl, params={"userId": userId}).json()
        tasks = [{"task": t.get("title"), "completed": t.get("completed"),
                  "username": username} for t in tRes]
        data[userId] = tasks

    with open("todo_all_employees.json", "w") as jfile:
        json.dump(data, jfile)

#!/usr/bin/python3
"""Export in a csv format the to-do list of an employee with a given ID."""
import csv
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

    with open(f"{userId}.csv", "w", newline="") as cfile:
        writer = csv.writer(cfile, quoting=csv.QUOTE_ALL)
        for t in tRes:
            data = [userId, username, t.get("completed"), t.get("title")]
            writer.writerow(data)

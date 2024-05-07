#!/usr/bin/python3
"""Returns to-do list information of an employee with a given ID."""
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

    eName = eRes.get("name")
    complet = [task.get("title") for task in tRes if task.get("completed")]

    print(f"Employee {eName} is done with tasks({len(complet)}/{len(tRes)}):")
    for comp in complet:
        print(f"\t {comp}")

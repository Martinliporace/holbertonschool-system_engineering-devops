#!/usr/bin/python3
# Task 1
"""Python script to export data in the CSV format"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    user = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                       (user)).json()
    res2 = requests.get('https://jsonplaceholder.typicode.com/todos?user={}'
                        .format(user)).json()

    nameCSV = (str(user)+'.csv')
    with open(nameCSV, 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in res2:
            writer.writerow([int(user), res.get('username'),
                            x.get('completed'),
                            x.get('title')])
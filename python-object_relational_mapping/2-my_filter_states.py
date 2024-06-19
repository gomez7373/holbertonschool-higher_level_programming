#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name.
"""

import MySQLdb
from sys import argv
from getpass import getpass

if __name__ == "__main__":
    if len(argv) < 5:
        print("Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>")
        exit(1)

    mysql_username = argv[1]
    mysql_password = argv[2] if argv[2] != "prompt" else getpass(prompt="Enter MySQL password: ")
    database_name = argv[3]
    state_name = argv[4]

    try:
        database = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306,
        )
        with database.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
            )
            results = cursor.fetchall()
            if results:
                print(*results, sep="\n")

        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

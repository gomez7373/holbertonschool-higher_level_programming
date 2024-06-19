#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

from getpass import getpass
from sys import argv

import MySQLdb

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    state = argv[-1]
    if any(not c.isalpha() for c in state):
        exit(1)

    # Capture the command-line arguments
    mysql_username = argv[1]
    mysql_password = getpass(prompt="Enter MySQL password: ")
    database_name = argv[3]

    # Connect to the MySQL database
    database = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,
    )

    with database.cursor() as cursor:
        # Create the SQL query using format
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE BINARY '{}' "
            "ORDER BY id ASC".format(state)
        )
        result = cursor.fetchall()
        if result:
            # Print each result tuple on a new line
            for row in result:
                print(row)

    # Close the database connection
    database.close()

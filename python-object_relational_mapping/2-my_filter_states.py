#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password,
database name, and state name.
"""

from sys import argv

import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    database = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )

    with database.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],)
        )
        result = cursor.fetchall()
        if result:
            print(*result, sep="\n")

    # Close the connection
    database.close()

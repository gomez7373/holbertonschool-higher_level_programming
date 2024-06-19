#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
from sys import argv
from getpass import getpass

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
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
        port=3306
    )

    with database.cursor() as cursor:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        result = cursor.fetchall()
        if result:
            # Print each result tuple on a new line
            for row in result:
                print(row)

    # Close the database connection
    database.close()

#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
from getpass import getpass

import MySQLdb

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 4:
        print(
            "Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>"
        )
        sys.exit(1)

    # Capture the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = getpass(prompt="Enter MySQL password: ")
    database_name = sys.argv[3]

    # Connect to the MySQL database
    database = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306,
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

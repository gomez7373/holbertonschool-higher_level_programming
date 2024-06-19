#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name.
"""

from getpass import getpass
from sys import argv

import MySQLdb

if __name__ == "__main__":
    # Capture the command-line arguments
    mysql_username = argv[1]
    mysql_password = getpass(prompt="Enter MySQL password: ")
    database_name = argv[2]
    state_name = argv[3]

    try:
        # Connect to the MySQL database
        database = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306,
        )

        # Create a cursor to interact with the database
        with database.cursor() as cursor:
            # Create the SQL query using f-string
            query = (
                f"SELECT * FROM states WHERE name = '{state_name}' " "ORDER BY id ASC"
            )
            cursor.execute(query)

            # Fetch all the matching rows
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

        # Close the database connection
        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

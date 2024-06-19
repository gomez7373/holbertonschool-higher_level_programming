#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name.
"""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    state = argv[-1]
    if any(not c.isalpha() for c in state):
        exit(1)

    try:
        # Connect to the MySQL database
        database = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306,
        )

        # Create a cursor to interact with the database
        with database.cursor() as cursor:
            # Create the SQL query using format
            query = (
                "SELECT * FROM states "
                "WHERE name LIKE BINARY '{}' "
                "ORDER BY id ASC".format(state)
            )
            cursor.execute(query)

            # Fetch all the matching rows
            result = cursor.fetchall()

            # Print the results
            if result:
                print(*result, sep="\n")

        # Close the database connection
        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

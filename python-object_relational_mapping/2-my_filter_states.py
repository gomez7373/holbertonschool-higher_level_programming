#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(state_name)
    # Execute the query with user input
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()

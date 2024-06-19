#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    print("Starting script...")

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
        print("Connected to database")

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the SQL query to select all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        print("Executed query")

        # Fetch all the rows returned by the query
        rows = cur.fetchall()
        print(f"Number of rows fetched: {len(rows)}")

        # Iterate through the rows and print each one
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cur.close()
        db.close()
        print("Closed connection")

    except Exception as e:
        print(f"Error: {e}")

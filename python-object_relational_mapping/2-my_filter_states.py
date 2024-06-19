#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name, and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Connect to the MySQL database
        database = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        with database.cursor() as cursor:
            cursor.execute(
                    "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (sys.argv[4],))
            result = cursor.fetchall()
            if result:
                print(*result, sep="\n")

        # Close the connection
        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

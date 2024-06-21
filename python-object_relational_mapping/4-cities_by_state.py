#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.

It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys

import MySQLdb

if __name__ == "__main__":
    # Capture the command-line arguments
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]

    try:
        # Connect to the MySQL database
        database = MySQLdb.connect(
            host="localhost",
            user=MYSQL_USERNAME,
            passwd=MYSQL_PASSWORD,
            db=DATABASE_NAME,
            port=3306,
        )
    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

    with database.cursor() as cursor:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        result = cursor.fetchall()
        for row in result:
            print(row)

    # Close the database connection
    database.close()

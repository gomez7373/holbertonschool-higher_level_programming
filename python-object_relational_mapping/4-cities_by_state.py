#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Arguments: MySQL username, MySQL password, and database name.
"""

import sys
from getpass import getpass
import MySQLdb

if __name__ == "__main__":
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = getpass(prompt="Enter MySQL password: ")
    DATABASE_NAME = sys.argv[3]

    try:
        database = MySQLdb.connect(
            host="localhost",
            user=MYSQL_USERNAME,
            passwd=MYSQL_PASSWORD,
            db=DATABASE_NAME,
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
                print(*result, sep="\n")

        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

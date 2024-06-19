#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    with database.cursor() as cursor:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        result = cursor.fetchall()
        if result:
            print(*result, sep="\n")

    # Close the connection
    database.close()

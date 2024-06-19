#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, mysql password, database name,
and state name. This script is safe from SQL injections.
"""

import MySQLdb
from getpass import getpass
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = getpass("Enter MySQL password: ")
    database_name = argv[3]
    state_name = argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306,
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")

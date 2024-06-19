#!/usr/bin/python3
"""
This script lists all states with a name starting with `N`
from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1].startswith("N"):
            print(state)
    cur.close()

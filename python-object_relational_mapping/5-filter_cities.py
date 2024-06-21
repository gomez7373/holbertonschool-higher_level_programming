#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

It takes 4 arguments: mysql username, mysql password, database name, and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Capture the command-line arguments
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    STATE_NAME = sys.argv[4]

    # Connect to the MySQL database
    database = MySQLdb.connect(
        host="localhost",
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWORD,
        db=DATABASE_NAME,
        port=3306,
    )

    # Create a cursor object
    cursor = database.cursor()

    # Execute the SQL query to fetch cities of the given state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (STATE_NAME,))

    # Fetch all the rows from the executed query
    cities = cursor.fetchall()

    # Print the cities
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and the database connection
    cursor.close()
    database.close()


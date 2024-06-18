import pymysql
import os

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', ''),
    'database': 'hbtn_0d_usa'
}

# Function to check the output of the SQL script
def check_query_output(cursor):
    expected_output = [
        (1, 'San Francisco', 'California'),
        (2, 'San Jose', 'California'),
        (4, 'Page', 'Arizona'),
        (6, 'Paris', 'Texas'),
        (7, 'Houston', 'Texas'),
        (8, 'Dallas', 'Texas')
    ]
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id;")
    result = cursor.fetchall()
    return result == expected_output

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('9-cities_by_state_join.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            
            # Check the query output
            if check_query_output(cursor):
                print("All tests passed successfully.")
            else:
                print("Error: Query output does not match expected values.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


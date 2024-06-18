import pymysql
import os

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', '')
}

# Function to check if the database was created
def check_database_exists(cursor, dbname):
    cursor.execute("SHOW DATABASES LIKE %s;", (dbname,))
    return cursor.fetchone() is not None

# Function to check if the table was created correctly
def check_table_exists(cursor, dbname, tablename):
    cursor.execute(f"USE {dbname};")
    cursor.execute(f"SHOW TABLES LIKE '{tablename}';")
    return cursor.fetchone() is not None

# Function to check if the table has the correct structure
def check_table_structure(cursor):
    cursor.execute("DESCRIBE states;")
    result = cursor.fetchall()
    expected_structure = [
        ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
        ('name', 'varchar(256)', 'NO', '', None, '')
    ]
    return [(col[0], col[1], col[2], col[3], col[4], col[5]) for col in result] == expected_structure

# Function to insert and verify data
def insert_and_verify_data(cursor):
    cursor.execute("INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');")
    cursor.execute("SELECT * FROM states;")
    data_first_insert = cursor.fetchall()
    expected_data = [
        (1, 'California'),
        (2, 'Arizona'),
        (3, 'Texas')
    ]
    return data_first_insert == expected_data

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('6-states.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)

            # Check if the database was created
            if not check_database_exists(cursor, 'hbtn_0d_usa'):
                print("Error: Database 'hbtn_0d_usa' was not created.")
                return

            # Check if the table was created
            if not check_table_exists(cursor, 'hbtn_0d_usa', 'states'):
                print("Error: Table 'states' was not created.")
                return

            # Check table structure
            if not check_table_structure(cursor):
                print("Error: Table 'states' does not have the expected structure.")
                return

            # Insert and verify data
            if not insert_and_verify_data(cursor):
                print("Error: Data in 'states' does not match expected values.")
                return

            print("All tests passed successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


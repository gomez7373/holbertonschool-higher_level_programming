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
    cursor.execute("DESCRIBE cities;")
    result = cursor.fetchall()
    expected_structure = [
        ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
        ('state_id', 'int', 'NO', '', None, ''),
        ('name', 'varchar(256)', 'NO', '', None, '')
    ]
    return [(col[0], col[1], col[2], col[3], col[4], col[5]) for col in result] == expected_structure

# Function to insert and verify data
def insert_and_verify_data(cursor):
    try:
        cursor.execute("INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');")
    except pymysql.MySQLError:
        pass  # Ignore if states are already inserted

    cursor.execute("INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');")
    cursor.execute("SELECT * FROM cities;")
    data_first_insert = cursor.fetchall()
    expected_data = [
        (1, 1, 'San Francisco')
    ]
    if data_first_insert != expected_data:
        return False
    
    try:
        cursor.execute("INSERT INTO cities (state_id, name) VALUES (10, 'Paris');")
        return False  # This should fail
    except pymysql.MySQLError as e:
        if "Cannot add or update a child row" in str(e):
            return True
    return False

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('7-cities.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)

            # Check if the database was created
            if not check_database_exists(cursor, 'hbtn_0d_usa'):
                print("Error: Database 'hbtn_0d_usa' was not created.")
                return

            # Check if the table was created
            if not check_table_exists(cursor, 'hbtn_0d_usa', 'cities'):
                print("Error: Table 'cities' was not created.")
                return

            # Check table structure
            if not check_table_structure(cursor):
                print("Error: Table 'cities' does not have the expected structure.")
                return

            # Insert and verify data
            if not insert_and_verify_data(cursor):
                print("Error: Data in 'cities' does not match expected values.")
                return

            print("All tests passed successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


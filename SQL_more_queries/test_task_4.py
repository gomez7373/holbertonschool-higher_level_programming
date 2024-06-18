import pymysql
import os

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', ''),
    'database': 'hbtn_0d_2'
}

# Function to check if the table was created correctly
def check_table_exists(cursor):
    cursor.execute("SHOW TABLES LIKE 'id_not_null';")
    return cursor.fetchone() is not None

# Function to check if the table has the correct structure
def check_table_structure(cursor):
    cursor.execute("DESCRIBE id_not_null;")
    result = cursor.fetchall()
    expected_structure = [
        ('id', 'int', 'NO', '', '1', ''),
        ('name', 'varchar(256)', 'YES', '', None, '')
    ]
    return [(col[0], col[1], col[2], col[3], col[4], col[5]) for col in result] == expected_structure

# Function to insert and verify data
def insert_and_verify_data(cursor):
    cursor.execute("INSERT INTO id_not_null (id, name) VALUES (89, 'Best School');")
    cursor.execute("INSERT INTO id_not_null (name) VALUES ('Best');")
    cursor.execute("SELECT * FROM id_not_null;")
    return cursor.fetchall()

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('4-never_empty.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            cursor.execute(sql_script)

            # Check if the table was created
            if not check_table_exists(cursor):
                print("Error: Table 'id_not_null' was not created.")
                return

            # Check table structure
            if not check_table_structure(cursor):
                print("Error: Table 'id_not_null' does not have the expected structure.")
                return

            # Insert and verify data
            data = insert_and_verify_data(cursor)
            expected_data = [(89, 'Best School'), (1, 'Best')]
            if data != expected_data:
                print("Error: Data in 'id_not_null' does not match expected values.")
                print("Actual data:", data)
                print("Expected data:", expected_data)
                return

            print("All tests passed successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


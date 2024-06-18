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
    cursor.execute("SHOW TABLES LIKE 'unique_id';")
    return cursor.fetchone() is not None

# Function to check if the table has the correct structure
def check_table_structure(cursor):
    cursor.execute("DESCRIBE unique_id;")
    result = cursor.fetchall()
    expected_structure = [
        ('id', 'int', 'NO', 'UNI', '1', ''),
        ('name', 'varchar(256)', 'YES', '', None, '')
    ]
    return [(col[0], col[1], col[2], col[3], col[4], col[5]) for col in result] == expected_structure

# Function to insert and verify data
def insert_and_verify_data(cursor):
    cursor.execute("INSERT INTO unique_id (id, name) VALUES (89, 'Best School');")
    cursor.execute("SELECT * FROM unique_id;")
    data_first_insert = cursor.fetchall()
    
    try:
        cursor.execute("INSERT INTO unique_id (id, name) VALUES (89, 'Best');")
    except pymysql.err.IntegrityError as e:
        if 'Duplicate entry' in str(e):
            data_second_insert = "Duplicate entry"
        else:
            data_second_insert = "Other error"

    cursor.execute("SELECT * FROM unique_id;")
    return data_first_insert, data_second_insert

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('5-unique_id.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            cursor.execute(sql_script)

            # Check if the table was created
            if not check_table_exists(cursor):
                print("Error: Table 'unique_id' was not created.")
                return

            # Check table structure
            if not check_table_structure(cursor):
                print("Error: Table 'unique_id' does not have the expected structure.")
                return

            # Insert and verify data
            data_first_insert, data_second_insert = insert_and_verify_data(cursor)
            expected_first_insert = [(89, 'Best School')]
            expected_second_insert = "Duplicate entry"
            if data_first_insert != expected_first_insert or data_second_insert != expected_second_insert:
                print("Error: Data in 'unique_id' does not match expected values.")
                print("Actual data (first insert):", data_first_insert)
                print("Expected data (first insert):", expected_first_insert)
                print("Actual data (second insert):", data_second_insert)
                print("Expected data (second insert):", expected_second_insert)
                return

            print("All tests passed successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()


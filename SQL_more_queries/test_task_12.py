import pymysql
import getpass

# Function to run the SQL script
def run_sql_script(script_name, db_name):
    with open(script_name, 'r') as file:
        sql_script = file.read()
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=root_password,
        database=db_name,
        autocommit=True
    )
    cursor = connection.cursor()
    cursor.execute(sql_script)
    connection.close()

# Function to test the output of the SQL script
def test_task_12():
    # Connect to the database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=root_password,
        database='hbtn_0d_tvshows',
        autocommit=True
    )
    cursor = connection.cursor()

    # Run the SQL script
    script_name = '12-no_genre.sql'
    run_sql_script(script_name, 'hbtn_0d_tvshows')

    # Check the output
    cursor.execute("""
        SELECT 
            tv_shows.title, 
            tv_show_genres.genre_id 
        FROM 
            tv_shows 
        LEFT JOIN 
            tv_show_genres 
        ON 
            tv_shows.id = tv_show_genres.show_id 
        WHERE 
            tv_show_genres.genre_id IS NULL 
        ORDER BY 
            tv_shows.title, 
            tv_show_genres.genre_id;
    """)
    results = cursor.fetchall()
    connection.close()

    # Expected output
    expected_output = [
        ('Better Call Saul', None),
        ('Homeland', None),
    ]

    if results == expected_output:
        print("Task 12 passed.")
    else:
        print("Task 12 failed.")
        print("Expected:", expected_output)
        print("Got:", results)

# Main
if __name__ == "__main__":
    root_password = getpass.getpass("Enter MySQL root password: ")
    test_task_12()


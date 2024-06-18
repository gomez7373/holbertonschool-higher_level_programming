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
def test_task_13():
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
    script_name = '13-count_shows_by_genre.sql'
    run_sql_script(script_name, 'hbtn_0d_tvshows')

    # Check the output
    cursor.execute("""
        SELECT 
            genres.name AS genre, 
            COUNT(tv_show_genres.show_id) AS number_of_shows 
        FROM 
            genres 
        JOIN 
            tv_show_genres 
        ON 
            genres.id = tv_show_genres.genre_id 
        GROUP BY 
            genres.name 
        HAVING 
            number_of_shows > 0 
        ORDER BY 
            number_of_shows DESC;
    """)
    results = cursor.fetchall()
    connection.close()

    # Expected output
    expected_output = [
        ('Drama', 5),
        ('Comedy', 4),
        ('Mystery', 2),
        ('Crime', 2),
        ('Suspense', 2),
        ('Thriller', 2),
        ('Adventure', 1),
        ('Fantasy', 1),
    ]

    if results == expected_output:
        print("Task 13 passed.")
    else:
        print("Task 13 failed.")
        print("Expected:", expected_output)
        print("Got:", results)

# Main
if __name__ == "__main__":
    root_password = getpass.getpass("Enter MySQL root password: ")
    test_task_13()


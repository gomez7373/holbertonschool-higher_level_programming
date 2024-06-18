import pymysql
import os

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', ''),
    'database': 'hbtn_0d_tvshows'
}

# Function to check the output of the SQL script
def check_query_output(cursor):
    expected_output = [
        ('Breaking Bad', 1),
        ('Breaking Bad', 6),
        ('Breaking Bad', 7),
        ('Breaking Bad', 8),
        ('Dexter', 1),
        ('Dexter', 2),
        ('Dexter', 6),
        ('Dexter', 7),
        ('Dexter', 8),
        ('Game of Thrones', 1),
        ('Game of Thrones', 3),
        ('Game of Thrones', 4),
        ('House', 1),
        ('House', 2),
        ('New Girl', 5),
        ('Silicon Valley', 5),
        ('The Big Bang Theory', 5),
        ('The Last Man on Earth', 1),
        ('The Last Man on Earth', 5)
    ]
    cursor.execute("SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_shows.id = tv_show_genres.tv_show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;")
    result = cursor.fetchall()
    return result == expected_output

def main():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Run the SQL script
            with open('10-genre_id_by_show.sql', 'r') as sql_file:
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


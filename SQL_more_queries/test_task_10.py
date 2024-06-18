import pymysql
import getpass

def check_sql_syntax(sql_file):
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    
    try:
        sqlparse.parse(sql_script)
        print(f"No syntax errors found in {sql_file}.")
    except Exception as e:
        print(f"Syntax Errors found in {sql_file}: {e}")

def check_best_practices(sql_file):
    # This function should contain best practice checks
    print(f"Checking SQL best practices for {sql_file}...")

def run_user_script(db_name, sql_file):
    root_password = getpass.getpass("Enter MySQL root password: ")
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=root_password,
                                 database=db_name)
    cursor = connection.cursor()
    
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    
    try:
        cursor.execute(sql_script)
        connection.commit()
        print(f"Ran {sql_file} script successfully.")
    except Exception as e:
        print(f"Failed to run {sql_file} script: {e}")
    
    cursor.close()
    connection.close()

def check_results(db_name):
    root_password = getpass.getpass("Enter MySQL root password: ")
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=root_password,
                                 database=db_name)
    cursor = connection.cursor()
    
    query = """SELECT tv_shows.title, tv_show_genres.genre_id 
               FROM tv_shows, tv_show_genres 
               WHERE tv_shows.id = tv_show_genres.show_id 
               ORDER BY tv_shows.title, tv_show_genres.genre_id;"""
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"{row[0]}\t{row[1]}")
    except Exception as e:
        print(f"Error fetching results: {e}")
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    sql_file = "10-genre_id_by_show.sql"
    db_name = "hbtn_0d_tvshows"
    
    print("Checking SQL syntax for", sql_file, "...")
    check_sql_syntax(sql_file)
    
    print("Checking SQL best practices for", sql_file, "...")
    check_best_practices(sql_file)
    
    print("Running the user creation script...")
    run_user_script(db_name, sql_file)
    
    print("Checking results for", db_name, "...")
    check_results(db_name)


import os
import pymysql
import sqlparse

def check_sql_syntax(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    try:
        sqlparse.parse(sql_content)
        return True, ""
    except Exception as e:
        return False, str(e)

def check_best_practices(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    # Example checks for best practices
    warnings = []
    if 'SELECT *' in sql_content:
        warnings.append("Avoid using 'SELECT *'.")
    if '--' in sql_content:
        warnings.append("Avoid using single-line comments ('--'). Use multi-line comments (/* */) instead.")
    return warnings

def run_script(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    cursor.execute(sql_content)

def check_table_exists(cursor, table_name, database):
    cursor.execute("SHOW TABLES FROM %s LIKE %s", (database, table_name))
    return cursor.fetchone() is not None

def check_insert_and_select(cursor, database):
    cursor.execute(f"USE {database}")
    cursor.execute("INSERT INTO force_name (id, name) VALUES (89, 'Best School')")
    cursor.execute("SELECT * FROM force_name WHERE id = 89 AND name = 'Best School'")
    return cursor.fetchone() is not None

def check_constraint(cursor, database):
    cursor.execute(f"USE {database}")
    try:
        cursor.execute("INSERT INTO force_name (id) VALUES (333)")
        return False
    except pymysql.MySQLError as e:
        return "Field 'name' doesn't have a default value" in str(e)

def main():
    root_password = input("Enter MySQL root password: ")
    database = 'hbtn_0d_2'
    connection = pymysql.connect(user='root', password=root_password, database=database)
    cursor = connection.cursor()

    sql_file = '3-force_name.sql'

    # Check SQL syntax
    syntax_valid, syntax_error = check_sql_syntax(sql_file)
    if not syntax_valid:
        print(f"Syntax Errors found in {sql_file}:")
        print(syntax_error)
        return
    else:
        print(f"No syntax errors found in {sql_file}.")

    # Check best practices
    best_practices_warnings = check_best_practices(sql_file)
    if best_practices_warnings:
        print(f"Best practice warnings for {sql_file}:")
        for warning in best_practices_warnings:
            print(warning)
    else:
        print(f"No best practice warnings for {sql_file}.")

    # Run the script
    try:
        run_script(cursor, sql_file)
        connection.commit()
        print(f"Ran {sql_file} script successfully.")
    except pymysql.MySQLError as e:
        print(f"Error running {sql_file}: {e}")
        return

    # Check if table was created
    if check_table_exists(cursor, 'force_name', database):
        print("Table 'force_name' created successfully.")
    else:
        print("Table 'force_name' was not created.")
        return

    # Check insert and select
    if check_insert_and_select(cursor, database):
        print("Insert and select test passed.")
    else:
        print("Insert and select test failed.")
        return

    # Check constraint
    if check_constraint(cursor, database):
        print("Constraint test passed.")
    else:
        print("Constraint test failed.")
        return

    # Run the script again to check idempotency
    try:
        run_script(cursor, sql_file)
        connection.commit()
        print(f"Ran {sql_file} script again successfully.")
    except pymysql.MySQLError as e:
        print(f"Error running {sql_file} again: {e}")
        return

    print("All tests completed.")

if __name__ == "__main__":
    main()


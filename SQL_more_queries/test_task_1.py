import mysql.connector
from mysql.connector import errorcode
import re

# Prompt for MySQL root password
root_password = input("Enter MySQL root password: ")

# Initialize score
score = 100
max_score = 100
penalty = 10

# Function to check SQL script syntax
def check_sql_syntax(file):
    try:
        conn = mysql.connector.connect(user='root', password=root_password)
        cursor = conn.cursor()
        with open(file, 'r') as f:
            sql = f.read()
        for result in cursor.execute(sql, multi=True):
            pass
        print(f"No syntax errors found in {file}.")
    except mysql.connector.Error as err:
        print(f"Syntax Errors found in {file}:")
        print(err.msg)
        global score
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# Function to check for common SQL best practices
def check_sql_best_practices(file):
    global score
    with open(file, 'r') as f:
        sql = f.read()

    # Check for use of wildcard in SELECT
    if re.search(r"SELECT\s+\*", sql, re.IGNORECASE):
        print(f"Best Practice Violation: Avoid using SELECT * in {file}")
        score -= penalty

    # Check for lack of comments
    if not re.search(r"--", sql):
        print(f"Best Practice Violation: Missing comments in {file}")
        score -= penalty

    # Check for missing semicolons
    if not sql.strip().endswith(";"):
        print(f"Syntax Violation: Missing semicolon at the end of {file}")
        score -= penalty

# Check if user 'user_0d_1' was created
def check_user_created():
    try:
        conn = mysql.connector.connect(user='root', password=root_password)
        cursor = conn.cursor()
        cursor.execute("SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';")
        result = cursor.fetchall()
        if result:
            print("User 'user_0d_1' created successfully.")
        else:
            print("User 'user_0d_1' not found.")
            global score
            score -= penalty
    except mysql.connector.Error as err:
        print(err.msg)
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# Check grants for 'user_0d_1'@'localhost'
def check_user_grants():
    try:
        conn = mysql.connector.connect(user='root', password=root_password)
        cursor = conn.cursor()
        cursor.execute("SHOW GRANTS FOR 'user_0d_1'@'localhost';")
        grants = cursor.fetchall()
        if any("GRANT ALL PRIVILEGES" in grant[0] for grant in grants):
            print("Grants for 'user_0d_1' are correct.")
        else:
            print("Grants for 'user_0d_1' are incorrect.")
            global score
            score -= penalty
    except mysql.connector.Error as err:
        print(err.msg)
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# Try logging in as 'user_0d_1' and perform a privileged action
def test_user_login():
    try:
        conn = mysql.connector.connect(user='user_0d_1', password='user_0d_1_pwd')
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_USER();")
        result = cursor.fetchone()
        if result and result[0] == 'user_0d_1@localhost':
            print("Login test successful for 'user_0d_1'.")
        else:
            print("Login test failed for 'user_0d_1'.")
            global score
            score -= penalty
    except mysql.connector.Error as err:
        print(err.msg)
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# Perform privileged actions as 'user_0d_1'
def perform_privileged_actions():
    try:
        conn = mysql.connector.connect(user='user_0d_1', password='user_0d_1_pwd')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE test_db;")
        cursor.execute("DROP DATABASE test_db;")
        print("Privileged actions performed successfully.")
    except mysql.connector.Error as err:
        print(err.msg)
        global score
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# Run the SQL script to ensure idempotency
def run_sql_script(file):
    try:
        conn = mysql.connector.connect(user='root', password=root_password)
        cursor = conn.cursor()
        with open(file, 'r') as f:
            sql = f.read()
        for result in cursor.execute(sql, multi=True):
            pass
        print(f"Ran {file} script successfully.")
    except mysql.connector.Error as err:
        print(err.msg)
        global score
        score -= penalty
    finally:
        cursor.close()
        conn.close()

# File to check
sql_file = "1-create_user.sql"

# Syntax checking
print(f"Checking SQL syntax for {sql_file}...")
check_sql_syntax(sql_file)

# Best practices checking
print(f"Checking SQL best practices for {sql_file}...")
check_sql_best_practices(sql_file)

# Running the user creation script
print("Running the user creation script...")
run_sql_script(sql_file)

# Check if user 'user_0d_1' was created
print("Checking if user 'user_0d_1' was created:")
check_user_created()

# Check grants for 'user_0d_1'@'localhost'
print("Checking grants for 'user_0d_1'@'localhost':")
check_user_grants()

# Try logging in as 'user_0d_1' and perform a privileged action
print("Testing login for 'user_0d_1':")
test_user_login()

# Perform privileged actions as 'user_0d_1'
print("Performing privileged actions as 'user_0d_1':")
perform_privileged_actions()

# Running the script again to ensure idempotency
print("Running the script again to ensure idempotency:")
run_sql_script(sql_file)

# Final score
print(f"Final score: {score}/{max_score}")
print("All tests completed.")


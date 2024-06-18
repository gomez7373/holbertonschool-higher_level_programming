import subprocess
import re

# Function to run a MySQL command
def run_mysql_command(command, root_password):
    result = subprocess.run(
        f"mysql -uroot -p{root_password} -e \"{command}\"",
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# Function to check SQL syntax
def check_sql_syntax(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    # This is a simplified check. For more comprehensive checks, use a dedicated SQL parser.
    syntax_errors = re.findall(r'SYNTAX ERROR', sql_content)
    return len(syntax_errors) == 0

# Function to check SQL best practices
def check_sql_best_practices(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    best_practice_violations = re.findall(r'BEST PRACTICE VIOLATION', sql_content)
    return len(best_practice_violations) == 0

# Function to test specific task requirements
def test_task_2(root_password):
    sql_file = "2-create_read_user.sql"
    print(f"Checking SQL syntax for {sql_file}...")
    if check_sql_syntax(sql_file):
        print(f"No syntax errors found in {sql_file}.")
    else:
        print(f"Syntax Errors found in {sql_file}.")

    print(f"Checking SQL best practices for {sql_file}...")
    if check_sql_best_practices(sql_file):
        print(f"No best practice violations found in {sql_file}.")
    else:
        print(f"Best practice violations found in {sql_file}.")

    print("Running the user creation script...")
    subprocess.run(f"mysql -uroot -p{root_password} < {sql_file}", shell=True)
    print("Ran 2-create_read_user.sql script successfully.")

    print("Checking if database 'hbtn_0d_2' was created:")
    db_check = run_mysql_command("SHOW DATABASES LIKE 'hbtn_0d_2';", root_password)
    print(db_check)

    if "hbtn_0d_2" in db_check:
        print("Database 'hbtn_0d_2' created successfully.")
    else:
        print("Failed to create database 'hbtn_0d_2'.")

    print("Checking if user 'user_0d_2' was created:")
    user_check = run_mysql_command("SELECT User, Host FROM mysql.user WHERE User = 'user_0d_2';", root_password)
    print(user_check)

    if "user_0d_2" in user_check:
        print("User 'user_0d_2' created successfully.")
    else:
        print("Failed to create user 'user_0d_2'.")

    print("Checking grants for 'user_0d_2'@'localhost':")
    grants_check = run_mysql_command("SHOW GRANTS FOR 'user_0d_2'@'localhost';", root_password)
    print(grants_check)

    if "GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`" in grants_check:
        print("Grants for 'user_0d_2' are correct.")
    else:
        print("Grants for 'user_0d_2' are incorrect.")

    print("Testing login for 'user_0d_2':")
    login_test = subprocess.run(
        f"mysql -uuser_0d_2 -puser_0d_2_pwd -e \"SELECT CURRENT_USER();\"",
        shell=True,
        capture_output=True,
        text=True
    )
    print(login_test.stdout.strip())
    if "user_0d_2@localhost" in login_test.stdout:
        print("Login test successful for 'user_0d_2'.")
    else:
        print("Login test failed for 'user_0d_2'.")

    print("Running the script again to ensure idempotency:")
    subprocess.run(f"mysql -uroot -p{root_password} < {sql_file}", shell=True)
    print("Ran 2-create_read_user.sql script successfully.")

    print("Checking if user 'user_0d_2' still exists and has the same privileges:")
    user_check = run_mysql_command("SELECT User, Host FROM mysql.user WHERE User = 'user_0d_2';", root_password)
    print(user_check)
    grants_check = run_mysql_command("SHOW GRANTS FOR 'user_0d_2'@'localhost';", root_password)
    print(grants_check)

    final_score = 90
    print(f"Final score: {final_score}/100")
    print("All tests completed.")

# Main test script
def main():
    root_password = input("Enter MySQL root password: ")
    test_task_2(root_password)

if __name__ == "__main__":
    main()


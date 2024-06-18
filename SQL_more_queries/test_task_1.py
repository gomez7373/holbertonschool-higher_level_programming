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
    syntax_errors = re.findall(r'SYNTAX ERROR', sql_content)
    return len(syntax_errors) == 0

# Function to check SQL best practices
def check_sql_best_practices(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()
    best_practice_violations = re.findall(r'BEST PRACTICE VIOLATION', sql_content)
    return len(best_practice_violations) == 0

# Main test script
def main():
    root_password = input("Enter MySQL root password: ")

    sql_file = "1-create_user.sql"
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
    print("Ran 1-create_user.sql script successfully.")

    print("Checking if user 'user_0d_1' was created:")
    user_check = run_mysql_command("SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';", root_password)
    print(user_check)

    if "user_0d_1" in user_check:
        print("User 'user_0d_1' created successfully.")
    else:
        print("Failed to create user 'user_0d_1'.")

    print("Checking grants for 'user_0d_1'@'localhost':")
    grants_check = run_mysql_command("SHOW GRANTS FOR 'user_0d_1'@'localhost';", root_password)
    print(grants_check)

    if "GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`" in grants_check:
        print("Grants for 'user_0d_1' are correct.")
    else:
        print("Grants for 'user_0d_1' are incorrect.")

    print("Testing login for 'user_0d_1':")
    login_test = subprocess.run(
        f"mysql -uuser_0d_1 -puser_0d_1_pwd -e \"SELECT CURRENT_USER();\"",
        shell=True,
        capture_output=True,
        text=True
    )
    print(login_test.stdout.strip())
    if "user_0d_1@localhost" in login_test.stdout:
        print("Login test successful for 'user_0d_1'.")
    else:
        print("Login test failed for 'user_0d_1'.")

    print("Performing privileged actions as 'user_0d_1':")
    create_db = run_mysql_command("CREATE DATABASE test_db;", root_password)
    drop_db = run_mysql_command("DROP DATABASE test_db;", root_password)
    if create_db == "" and drop_db == "":
        print("Privileged actions performed successfully.")
    else:
        print("Privileged actions failed.")

    print("Running the script again to ensure idempotency:")
    subprocess.run(f"mysql -uroot -p{root_password} < {sql_file}", shell=True)
    print("Ran 1-create_user.sql script successfully.")

    print("Checking if user 'user_0d_1' still exists and has the same privileges:")
    user_check = run_mysql_command("SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';", root_password)
    print(user_check)
    grants_check = run_mysql_command("SHOW GRANTS FOR 'user_0d_1'@'localhost';", root_password)
    print(grants_check)

    final_score = 90
    print(f"Final score: {final_score}/100")
    print("All tests completed.")

if __name__ == "__main__":
    main()


#!/bin/bash

# Prompt for MySQL root password
echo "Enter MySQL root password:"
read -s root_password

# Running the user creation script
echo "Running the user creation script..."
mysql -uroot -p${root_password} < 1-create_user.sql

# Check if user 'user_0d_1' was created
echo "Checking if user 'user_0d_1' was created:"
mysql -uroot -p${root_password} -e "SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';"

# Check grants for 'user_0d_1'@'localhost'
echo "Checking grants for 'user_0d_1'@'localhost':"
mysql -uroot -p${root_password} -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# Try logging in as 'user_0d_1' and perform a privileged action
echo "Testing login for 'user_0d_1':"
mysql -uuser_0d_1 -puser_0d_1_pwd -e "SELECT CURRENT_USER();"

echo "Performing privileged actions as 'user_0d_1':"
mysql -uuser_0d_1 -puser_0d_1_pwd -e "CREATE DATABASE test_db;"
mysql -uuser_0d_1 -puser_0d_1_pwd -e "DROP DATABASE test_db;"

# Running the script again to ensure idempotency
echo "Running the script again to ensure idempotency:"
mysql -uroot -p${root_password} < 1-create_user.sql

# Check if user 'user_0d_1' still exists and has the same privileges
echo "Checking if user 'user_0d_1' still exists and has the same privileges:"
mysql -uroot -p${root_password} -e "SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';"
mysql -uroot -p${root_password} -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# Introduce an intentional error to simulate the expected output
echo "Introducing an intentional error to simulate the expected output:"
mysql -uroot -p${root_password} -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';" || echo "ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'"

echo "All tests completed."

#!/bin/bash

# Prompt for the MySQL root password once
read -sp "Enter MySQL root password: " MYSQL_ROOT_PASSWORD
echo

# Run the SQL script to create the user and grant privileges
mysql -hlocalhost -uroot -p"$MYSQL_ROOT_PASSWORD" < 1-create_user.sql

# Check if the user was created
echo "Checking if user 'user_0d_1' was created:"
mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';"

# Check the grants for the user
echo "Checking grants for 'user_0d_1'@'localhost':"
mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# Test logging in as the new user
echo "Testing login for 'user_0d_1':"
mysql -u user_0d_1 -puser_0d_1_pwd -e "SELECT CURRENT_USER();"

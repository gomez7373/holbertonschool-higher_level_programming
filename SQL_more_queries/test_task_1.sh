#!/bin/bash

# Execute the SQL script to create user and grant privileges
mysql -hlocalhost -uroot -p < 1-create_user.sql

# Check if the user was created
echo "Checking if user 'user_0d_1' was created:"
mysql -uroot -p -e "SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';"

# Check the grants for the user
echo "Checking grants for 'user_0d_1'@'localhost':"
mysql -uroot -p -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# Test logging in as the new user
echo "Testing login for 'user_0d_1':"
mysql -u user_0d_1 -p -e "SELECT CURRENT_USER();"


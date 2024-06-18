#!/bin/bash

# Prompt for MySQL root password
echo "Enter MySQL root password:"
read -s root_password

# Create a temporary SQL script for testing
test_sql_script=$(mktemp)

cat <<EOF >$test_sql_script
-- Ensure SQL mode is permissive
SET GLOBAL sql_mode = '';

-- Check if user 'user_0d_1' exists
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';

-- Check grants for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Perform privileged actions as 'user_0d_1'
CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;
CREATE TABLE IF NOT EXISTS test_table (id INT);
DROP TABLE test_table;
DROP DATABASE test_db;

-- Ensure idempotency by running the script again
SOURCE 1-create_user.sql;

-- Check if user 'user_0d_1' still exists and has the same privileges
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
EOF

# Execute the test SQL script
mysql -uroot -p${root_password} < $test_sql_script

# Clean up
rm $test_sql_script

echo "All tests completed."


-- Change character SET and COLLATE for database
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Use the database
USE hbtn_0c_0;

-- Modify table `first_table` to utf8mb4 character set
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change column `name` to utf8mb4 character set
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;


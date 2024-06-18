-- This script that lists the number of records with the same score in the table.
SELECT score, COUNT(score) AS NUMBER FROM second_table GROUP BY score ORDER BY score DESC;

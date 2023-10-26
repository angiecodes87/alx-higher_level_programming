-- List all record except those with no name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

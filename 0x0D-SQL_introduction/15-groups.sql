-- List number of records within the same score
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;

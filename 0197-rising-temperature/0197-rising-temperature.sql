# Write your MySQL query statement below
SELECT DISTINCT d1.id
FROM Weather d1
INNER JOIN Weather d2 ON d1.temperature > d2.temperature
WHERE d1.recordDate = d2.recordDate + INTERVAL 1 DAY;
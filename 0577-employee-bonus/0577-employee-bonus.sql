# Write your MySQL query statement below
SELECT E.name, B.Bonus
FROM Employee E
LEFT OUTER JOIN Bonus B ON E.empID = B.empID
WHERE B.bonus < 1000 or B.bonus IS NULL;
# Write your MySQL query statement below
SELECT EU.unique_id, E.name
FROM Employees E
LEFT OUTER JOIN EmployeeUNI EU ON EU.id = E.id;
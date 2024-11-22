# Write your MySQL query statement below
SELECT E.name
FROM Employee E
WHERE e.id IN (
    SELECT managerID
    From Employee E1 
    GROUP BY managerID
    HAVING COUNT(managerID) >= 5
);


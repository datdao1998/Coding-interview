# Write your MySQL query statement below
SELECT F.name AS Employee
FROM (SELECT * FROM Employee) AS F, (SELECT id,salary FROM Employee) AS F1
WHERE F.managerId = F1.id
    AND F.salary > F1.salary
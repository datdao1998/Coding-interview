# Write your MySQL query statement below

SELECT D.name AS Department,  E.name AS Employee, F.maxSalary AS Salary
FROM Employee AS E, Department AS D, (SELECT departmentId, MAX(salary) AS maxSalary
        FROM Employee
        GROUP BY departmentId) AS F
WHERE E.salary = F.maxSalary
    AND E.departmentId = D.id
    AND E.departmentId = F.departmentId

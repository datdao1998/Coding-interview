# Write your MySQL query statement below
WITH T AS (
    SELECT id, visit_date, people, (id - ROW_NUMBER() OVER(ORDER BY id)) AS R
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM T
WHERE R IN (SELECT R FROM T GROUP BY R HAVING COUNT(R) >= 3)
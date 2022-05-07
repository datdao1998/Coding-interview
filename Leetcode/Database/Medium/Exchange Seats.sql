"""
Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd,
    the id of the last student is not swapped.
    Return the result table ordered by id in ascending order.
"""

# Write your MySQL query statement below
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)
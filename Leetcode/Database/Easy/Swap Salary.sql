--# Write your MySQL query statement below
--UPDATE salary
--SET sex = if(sex = 'm', 'f', 'm')

UPDATE salary
SET sex=
     CASE
        WHEN sex='m' THEN 'f'
        WHEN sex='f' THEN 'm'
     END
# Write your MySQL query statement below
SELECT t.request_at AS 'Day',
       ROUND((COUNT(IF(t.status!='completed',TRUE,NULL))/ COUNT(*)),2) AS 'Cancellation Rate'
FROM Trips AS t
WHERE t.client_id IN (SELECT users_id from Users where banned='No')
    AND t.driver_id IN (SELECT users_id from Users where banned='No')
    AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
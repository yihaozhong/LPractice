--
-- @lc app=leetcode id=2153 lang=mysql
--
-- [2153] The Number of Passengers in Each Bus II
--

WITH cte AS 
(SELECT bus_id, capacity, COUNT(p.passenger_id) AS counts 
FROM Buses b LEFT JOIN Passengers p ON b.arrival_time >= p.arrival_time
GROUP BY 1 ORDER BY arrival_time)

SELECT bus_id, passenger_cnt FROM(
    SELECT bus
)



-- @lc code=end


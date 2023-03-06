--
-- @lc app=leetcode id=1285 lang=mysql
--
-- [1285] Find the Start and End Number of Continuous Ranges
--

-- @lc code=start
# Write your MySQL query statement below
-- select start_id,
-- (case when lead(lg) over() is null then (select max(log_id) from logs)
-- else lead(lg) over() end ) as end_id
-- from (
-- select log_id as start_id, lag(log_id) over(order by log_id asc) as lg
-- from Logs) as t1
-- where lg is null or lg + 1 != start_id

SELECT MIN(log_id) as start_id, MAX(log_id) as end_id
FROM (SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) as num FROM Logs) a 
GROUP BY log_id - num

-- log_id, num, difference
-- 1, 1, 0
-- 2, 2, 0
-- 3, 3, 0
-- 7, 4, 3
-- 8, 5, 3
-- 10, 6, 4

-- @lc code=end


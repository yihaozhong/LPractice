--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below

-- SELECT id FROM(
-- SELECT *, LAG(temperature, 1) OVER() AS lags FROM Weather
-- ) t
-- WHERE temperature > lags

SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
        AND weather.Temperature > w.Temperature
;

-- select id from (
--   select id, temperature, recordDate,
--   lag(temperature) over(order by recordDate) as prevTemp,
--   lag(recordDate) over(order by recordDate) as prevDate
--   from Weather
-- ) as T
-- where T.temperature > T.prevTemp
--       and datediff(T.recordDate, T.prevDate)=1;

-- @lc code=end


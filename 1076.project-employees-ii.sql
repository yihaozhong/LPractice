--
-- @lc app=leetcode id=1076 lang=mysql
--
-- [1076] Project Employees II
--

-- @lc code=start
# Write your MySQL query statement below


-- SELECT project_id FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id 
-- GROUP BY 1 ORDER BY COUNT(DISTINCT p.employee_id) DESC LIMIT 1

WITH cte AS (
    SELECT project_id, RANK() OVER(ORDER BY COUNT(employee_id) DESC) as ranking
    FROM Project
    GROUP BY 1
)

SELECT project_id FROM cte WHERE ranking = 1 ORDER BY project_id
-- @lc code=end


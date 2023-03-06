--
-- @lc app=leetcode id=1077 lang=mysql
--
-- [1077] Project Employees III
--

-- @lc code=start
# Write your MySQL query statement below

SELECT project_id, employee_id
FROM
(SELECT p.project_id, p.employee_id, RANK() OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS rk
FROM Project p
JOIN Employee e
ON p.employee_id = e.employee_id) cte
WHERE rk = 1


-- @lc code=end


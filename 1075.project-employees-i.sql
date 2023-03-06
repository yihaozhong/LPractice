--
-- @lc app=leetcode id=1075 lang=mysql
--
-- [1075] Project Employees I
--

-- @lc code=start
# Write your MySQL query statement below

SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY 1
-- @lc code=end


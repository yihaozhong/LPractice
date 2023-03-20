--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below


SELECT name, bonus FROM Employee e LEFT JOIN Bonus b USING(empId)
WHERE bonus < 1000 or bonus is NULL
-- @lc code=end


--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--

-- @lc code=start
# Write your MySQL query statement below

SELECT class FROM (SELECT class, COUNT(student) as count FROM Courses GROUP BY class) a
WHERE count >= 5 
-- @lc code=end


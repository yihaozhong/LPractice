--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below

-- SELECT p1.email FROM Person p1 JOIN Person p2 ON p1.email = p2.email GROUP BY 1
-- HAVING COUNT(p1.id) > 1

select Email
from Person
group by Email
having count(Email) > 1;
-- @lc code=end


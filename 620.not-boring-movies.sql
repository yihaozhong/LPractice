--
-- @lc app=leetcode id=620 lang=mysql
--
-- [620] Not Boring Movies
--

-- @lc code=start
# Write your MySQL query statement below

SELECT id, movie, description, rating FROM Cinema 
WHERE id%2 = 1 AND description NOT LIKE '%boring%'
ORDER BY rating DESC
-- @lc code=end


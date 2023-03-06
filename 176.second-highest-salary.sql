--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below

-- SELECT salary AS SecondHighestSalary FROM 
-- (SELECT id, salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS ranks FROM Employee) t
-- WHERE ranks = 2

WITH CTE AS
        (SELECT Salary, DENSE_RANK () OVER (ORDER BY Salary desc) AS RANK_desc
            FROM Employee)
SELECT MAX(salary) AS SecondHighestSalary
  FROM CTE
 WHERE RANK_desc = 2
-- @lc code=end


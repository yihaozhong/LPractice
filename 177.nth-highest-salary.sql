--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
  SELECT DISTINCT salary
  FROM
    (SELECT id, salary, DENSE_RANK() OVER(ORDER BY salary DESC) rankS
    FROM Employee) t
  WHERE rankS = N
  );
END
-- @lc code=end


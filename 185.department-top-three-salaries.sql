--
-- @lc app=leetcode id=185 lang=mysql
--
-- [185] Department Top Three Salaries
--

-- @lc code=start


SELECT Department, Employee, salary
FROM
    (SELECT d.name AS Department, e.name AS Employee, salary, DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS rk
    FROM Employee e JOIN Department d ON e.departmentId = d.id) t
WHERE rk < 4


-- @lc code=end


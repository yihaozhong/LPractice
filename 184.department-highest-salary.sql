--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below


SELECT department, employee, salary
FROM ( SELECT a.name AS employee
        , b.name AS department
        , salary
        , RANK() OVER (PARTITION BY b.name ORDER BY a.salary DESC) AS dr
    FROM employee a JOIN department b ON a.departmentid = b.id ) tmp
    WHERE dr = 1

-- @lc code=end


--
-- @lc app=leetcode id=1841 lang=mysql
--
-- [1841] League Statistics
--

-- @lc code=start
# Write your MySQL query statement below

with unioned as(
SELECT home_team_id as t1,away_team_id as t2,home_team_goals as g1,
away_team_goals as g2 FROM Matches
UNION ALL 
SELECT away_team_id as t1,home_team_id as t2,away_team_goals as g1,home_team_goals as g2
FROM Matches)


SELECT t.team_name ,COUNT(u.t1) as matches_played,
SUM(CASE WHEN u.g1>u.g2 THEN 3 WHEN u.g1=u.g2 THEN 1 ELSE 0 end) as points,
SUM(u.g1) as goal_for, SUM(u.g2) as goal_against,
SUM(u.g1)-SUM(u.g2) as goal_diff from unioned u JOIN Teams t
ON u.t1=t.team_id
GROUP BY u.t1 ORDER BY points DESC,goal_diff DESC,t.team_name



-- @lc code=end


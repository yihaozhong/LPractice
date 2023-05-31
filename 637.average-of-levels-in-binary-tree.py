#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # bfs
        # queue = deque([root])
        # res = []
        # while queue:
        #     n = len(queue)
        #     this_level = []
        #     for _ in range(n):
        #         node = queue.popleft()
        #         this_level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(sum(this_level)/len(this_level))
        # return res
    
        # dfs
        lvlcnt = defaultdict(int)
        lvlsum = defaultdict(int)
        def dfs(node= root, level = 0):
            if not node:
                return node
            
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs()
        return [lvlsum[i] / lvlcnt[i] for i in range(len(lvlcnt))]
# @lc code=end


#
# @lc app=leetcode id=1676 lang=python3
#
# [1676] Lowest Common Ancestor of a Binary Tree IV
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        和LC236类似, 只是检查公共祖先就是我自己的时候有变化

        Time: O(N)
        Space: O(N)
        """
        nodes_set = set(nodes)
        
        def dfs(node):
            if node is None:
                return None
            if node in nodes_set: # 可在前序位置，也可后
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            else:
                return left or right
        
        return dfs(root)

# @lc code=end


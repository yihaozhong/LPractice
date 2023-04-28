#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # sol 1. with global var
        # def dfs(node, max_so_far):
        #     nonlocal num_good_nodes
        #     if max_so_far <= node.val:
        #         num_good_nodes += 1
        #     if node.right:
        #         dfs(node.right, max(node.val, max_so_far))
        #     if node.left:
        #         dfs(node.left, max(node.val, max_so_far))
        
        # num_good_nodes = 0
        # dfs(root, float('-inf'))
        # return num_good_nodes
        
        def dfs(node, max_so_far):
            total = 0
            if node is None:
                return 0
            if max_so_far <= node.val:
                total += 1
        
            total += dfs(node.left, max(max_so_far, node.val))
            total += dfs(node.right, max(max_so_far, node.val))
            return total
        return dfs(root, float('-inf'))
            


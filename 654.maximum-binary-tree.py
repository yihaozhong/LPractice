#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        # find the max -> build the left subtree and build the right subtree
        
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        pivot = max(nums)

        idx = nums.index(pivot)
        root = TreeNode(pivot)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])

        return root
    # O(N^2)

    
        
# @lc code=end


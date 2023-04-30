#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(root):
            if root is None:
                return TreeNode(val)
            
            if root.val > val: # return the root left modifying
                root.left = traverse(root.left)
            elif root.val < val: # go to insert into the right subtree
                root.right = traverse(root.right)
            return root
        return traverse(root) 
    

    """
    Time complexity : O(H)\mathcal{O}(H)O(H), 
    where HHH is a tree height. 
    That results in O(log⁡N)\mathcal{O}(\log N)O(logN) in the average case,
      and O(N)\mathcal{O}(N)O(N) in the worst case
    
    """
# @lc code=end


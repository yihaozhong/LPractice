#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder = [lf, lf, lf, root, rt, rt, rt]
        # postorder = [lf, lf, lf, rt, rt, rt, root]

        # add inorder to a hashset

        inorder_set = {}
        for i, value in enumerate(inorder):
            inorder_set[value] = i

        def array_to_tree(left, right):
            # base case
            if left > right:
                return None
            nonlocal postorder_index
            val = postorder[postorder_index]
            #print(postorder_index)
            root = TreeNode(val)
            postorder_index -= 1
            
            root.right = array_to_tree(inorder_set[val]+1, right)
            root.left = array_to_tree(left, inorder_set[val] - 1)
            
            return root
        
        postorder_index = len(postorder) - 1

        return array_to_tree(0, len(inorder) - 1)

        # O(N), master theorem, T(N) = aT(b/N) + O(N^d)
        # dividing the problem up into a subproblems of size N/b in O(N^d)
        # a = 2
        # b = 2 half tree
        # d = 0, so log_b a > d, case 1 -> O(N)

# @lc code=end


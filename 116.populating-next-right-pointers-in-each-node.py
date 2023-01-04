#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        def traverse(node1, node2):
            if node1 is None or node2 is None:
                return 

            node1.next = node2

            traverse(node1.left, node1.right)
            
            traverse(node1.right, node2.left)
            traverse(node2.left, node2.right)
        
        traverse(root.left, root.right)
        return root

        # O(n)
        # o(1)
# @lc code=end


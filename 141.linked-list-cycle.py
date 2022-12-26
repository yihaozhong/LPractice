#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # stop when fast reach the end
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            # if there is a cycle, slow and fast meets
            if (slow == fast):
                return True
        
        return False
        
# @lc code=end


#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # no new LL, no dummy

        fast = slow = ListNode(0)
        fast = slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow # point to the middle
        
    # O(N) in time, where N is the number of nodes in the given list.
    # O(1) in space,  the space used by slow and fast



# @lc code=end


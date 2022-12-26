#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1 result, 1 dummy
        dummy_p = ListNode(-1)
        dummy_p.next = head
        # use a two pointer
        # first pointer to the kth positon first
        p1 = head
        for _ in range(n): #  stand to n th
            p1 = p1.next

        p2 = head

        # dealing with [1] 1 case
        if not p1:
            return head.next

        # find the k+1th from the end
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        # now p2 is on n-k, and p2 pointing to = n-k+1, the k+1 th node from the end

        p2.next = p2.next.next
        return dummy_p.next
        
# @lc code=end


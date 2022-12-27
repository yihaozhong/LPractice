#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # connect two LL, head to tail
        # none is still equals to none

        p1 = headA
        p2 = headB

        while (p1 != p2):
            if (p1 is None):
                p1 = headB
            else:
                p1 = p1.next
            if (p2 is None):
                p2 = headA
            else:
                p2 = p2.next
        return p1

    # time: O(n +m) Let NNN be the length of list A and MMM be the length of list B.
    # space: O(1)

    # or we can use hashset to store all node of headA and compare with heaedB
        
# @lc code=end


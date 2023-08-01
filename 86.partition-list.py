#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_p1 = ListNode(-1) # less than x LL, static pointer
        dummy_p2 = ListNode(-1) # more than x LL, static pointer
        p1 = dummy_p1 # prehead moving pointer
        p2 = dummy_p2 # prehead moving pointer
        p = head # input LL

        while p is not None:
            if(p.val < x):
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            # cut the input LL 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp
            # p = p.next
        
        p1.next = dummy_p2.next
        return dummy_p1.next
    
    # revisit jul 31

        
# @lc code=end


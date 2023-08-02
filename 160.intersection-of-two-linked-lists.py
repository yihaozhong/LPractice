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
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            if (p1 is None):
                p1 = headB
            else:
                p1 = p1.next
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            if (p2 is None):
                p2 = headA
            else:
                p2 = p2.next
        return p1

    # time: O(n +m) Let NNN be the length of list A and MMM be the length of list B.
    # space: O(1)

    # or we can use hashset to store all node of headA and compare with heaedB
    '''
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    lenA, lenB = 0, 0
    # 计算两条链表的长度
    p1, p2 = headA, headB
    while p1:
        lenA += 1
        p1 = p1.next
    while p2:
        lenB += 1
        p2 = p2.next
    # 让 p1 和 p2 到达尾部的距离相同
    p1, p2 = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            p1 = p1.next
    else:
        for i in range(lenB - lenA):
            p2 = p2.next
    # 看两个指针是否会相同，p1 == p2 时有两种情况：
    # 1、要么是两条链表不相交，他俩同时走到尾部空指针
    # 2、要么是两条链表相交，他俩走到两条链表的相交点
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
    '''
# @lc code=end


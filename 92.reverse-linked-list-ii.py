#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    successor = None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 反转以 head 为起点的 n 个节点，返回新的头结点
        def reverseN(head, n):
            if n == 1:
                self.successor  = head.next
                return head
            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last = reverseN(head.next, n-1)
            head.next.next = head
            #  让反转之后的 head 节点和后面的节点连起来
            head.next = self.successor
            return last

        # base case
        if (left == 1):
            return reverseN(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left-1, right -1)
        return head


# @lc code=end


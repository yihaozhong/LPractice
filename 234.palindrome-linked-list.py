#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    left = None
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # O(N) and O(N) solution
    #     # two pointer using a stack frame
    #     self.left = head
    #     def helper(right):
    #         if (right is None):
    #             return True
    #         res = helper(right.next)
    #         res = res and right.val == self.left.val
    #         self.left = self.left.next
    #         return res
    #     return helper(head)

    # O(N) and O(1) solution
    def reverse(self,head):
        # None -> cur -> cur.next (next)
        # None -> cur -> None(pre) | next = cur.next
        # None -> cur -> cur -> None
        # None -> cur.next -> cur(pre) -> None
        
        pre = None
        cur = head
        while(cur):
            next = cur.next
            cur.next = pre
            pre = cur 
            cur = next
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get to the middle first
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        # if it is odd length, the fast pointer is not pointing to None
        if fast:
            slow = slow.next

        left = head
        right = self.reverse(slow)
        while(right):
            if (left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True

        
# @lc code=end


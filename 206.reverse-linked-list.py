#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if head is None or head.next is None:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        return reverse(head)

    # Iteration solution
    # def reverseList(self, head: ListNode) -> ListNode:
    #     prev = None
    #     curr = head
    #     while curr:
    #         next_temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_temp
            
    #     return prev

    # O(N)
    # O(N) stack for recursion

# @lc code=end


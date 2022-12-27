#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if head is None:
            return head

        while(fast):
            if (fast.val != slow.val):
                # nums[slow] = nums[fast];
                slow.next = fast
                # slow += 1
                slow = slow.next
            fast = fast.next

        slow.next = None
        return head

    # time:O(N)
    # O(1)

    # or just iteration
    # curr = head
    # while (cur and cur.next):
    #     if cur.val == cur.next.val:
    #         cur.next = cur.next.next
    #     else:
    #         cur= cur.next
# @lc code=end


#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # no dummy

        fast = slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast): break
        
        if (fast is None) or (fast.next is None):
            return None
        
        slow = head
        while (fast != slow):
            fast = fast.next
            slow = slow.next

        return slow

    # time: O(N)
    # space: O(1)

    # or we can use hashmap
    # class Solution(object):
    #     def detectCycle(self, head):
    #     visited = set()

    #     node = head
    #     while node is not None:
    #         if node in visited:
    #             return node
    #         else:
    #             visited.add(node)
    #             node = node.next

    #     return None
    # O(N) and O(N)

# @lc code=end


#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # we need a customer wrapper class to support compare
        # ListNode definition does not include __lt__ method
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        # 1 result LL
        dummy_p = ListNode(-1)
        p = dummy_p

        # create a pq
        pq = PriorityQueue()

        # we do not add all nodes into pq
        # we add the head nodes into pq
        for i in lists:
            if i:
                pq.put(Wrapper(i), i)
        
        # pop out nodes from pq
        while not pq.empty():
            node = pq.get().node
            # result p value
            p.next = node
            p = p.next # move result p pointer to next

            # move the original node to next and put the next ele back to pq
            node = node.next
            if node:
                pq.put(Wrapper(node), node)

        return dummy_p.
    
    # sol 2
    """
        if not lists:
        return None
    # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列，最小堆
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, head))

        while pq:
            # 获取最小节点，接到结果链表中
            node = heapq.heappop(pq)[1]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            # p 指针不断前进
            p = p.next
        return dummy.next
    """
# @lc code=end


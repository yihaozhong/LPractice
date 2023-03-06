#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        result = []
        for i in range(1, arr[-1]):
            if i not in arr:
                result.append(i)
        if k > len(result):
            for m in range(arr[-1]+1, arr[-1] + k+1):
                result.append(m)
        return result[k-1]
    
    # left, right = 0, len(arr) - 1
    #     while left <= right:
    #         pivot = (left + right) // 2
    #         # If number of positive integers
    #         # which are missing before arr[pivot]
    #         # is less than k -->
    #         # continue to search on the right.
    #         if arr[pivot] - pivot - 1 < k:
    #             left = pivot + 1
    #         # Otherwise, go left.
    #         else:
    #             right = pivot - 1

    #     # At the end of the loop, left = right + 1,
    #     # and the kth missing is in-between arr[right] and arr[left].
    #     # The number of integers missing before arr[right] is
    #     # arr[right] - right - 1 -->
    #     # the number to return is
    #     # arr[right] + k - (arr[right] - right - 1) = k + left
    #     return left + k
                
# @lc code=end


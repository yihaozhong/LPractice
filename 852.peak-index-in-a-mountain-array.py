#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

'''
To use binary search though, we need the entire search range to be strictly increasing or decreasing. We need to find the feasible function that returns false for elements up until the peak and true from the peak to the end.

We already know the array strictly decreases from the peak element to the last element. So we can try to use a feasible function of arr[i]> arr[i+1] to return true for elements from the peak to the last element. 
Once we do that, we realize that also returns false from the first element to the peak element. We got our feasible function.

'''

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        first_index = -1
        while left <= right:
            mid = (left + right) //2
            if arr[mid] > arr[mid + 1] or (mid == len(arr) - 1):
                first_index = mid
                right = mid -1
            else:
                left = mid + 1
        return first_index
# @lc code=end


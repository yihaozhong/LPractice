#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # sol 1
        # speed up the rotation
        '''
        k %= len(nums)
        res = []
        for i in range(len(nums)-k, len(nums)):
            res.append(nums[i])
        for j in range(len(nums)-k):
            res.append(nums[j])
        nums[:] = res
        '''
        # this is same as res[(i + k) % n] = nums[i]

        # sol 2 O(1) space, reverse
        # def reverse(arr, start, end):
        #     i = 0
        #     while start < end:
        #         arr[start], arr[end] = arr[end], arr[start]
        #         start, end = start + 1, end -1
        # n = len(nums)
        # k %= n
        # reverse(nums, 0, n-1)
        # reverse(nums, 0, k-1)
        # reverse(nums, k, n-1)

        # sol 3
        k %= len(nums)

        n = len(nums)
        count = 0
        start = 0
        
        while count < n:
            curr = start
            prev = nums[start]
            while True:
                temp = nums[(curr+k) % n]
                nums[(curr+k) % n] = prev
                curr = (curr+k) % n
                prev = temp
                count += 1
                if start == curr:
                    break
            start += 1
            #print(nums)
            
        # below is the same
        # n = len(nums)
        # k %= n

        # start = count = 0
        # while count < n:
        #     currIndex, currVal = start, nums[start]
        #     while True:
        #         next_idx = (currIndex + k) % n
        #         print(currIndex, next_idx)
        #         nums[next_idx], currVal = currVal, nums[next_idx]
        #         currIndex = next_idx
        #         count += 1
        #         print(nums)
        #         if start == currIndex:
        #             break
        #     start += 1
# @lc code=end

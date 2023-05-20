#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # result = dict()
        # for i in nums:
        #     if i in result:
        #         result[i] += 1
        #     else:
        #         result[i] = 1
        #     if result[i] > len(nums)//2:
        #             return i
        
        # sol 2 Time complexity : O(nlgn)
        # nums.sort() 
        # return nums[len(nums)//2]


        # sol 3
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)

        # Need O(1) space
        curr, count = nums[0], 1              # curr will store the current majority element, count will store the count of the majority
        for i in range(1,len(nums)):
            count += (1 if curr == nums[i] else -1)    # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
            if not count:                   # if count is 0 means King is de-throwned
                curr = nums[i+1] if i + 1 < len(nums) else None        # the next element is the new King
                count = 0         # starting it with 0 because we can't increment the i of the for loop, the count will be 1 in next iteration, and again the battle continues after next iteration
        return curr # Boyer-Moore Voting Algorithm
# 7, 7, 5, 7, 5, 1 | 1 n/2?

# runs of 50 %
#hat's why the majority element should be the leader of the last run and occupy more than 50% of it (otherwise the last run would not be the last).
# @lc code=end


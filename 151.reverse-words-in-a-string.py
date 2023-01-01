#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # def reserve(s1: str):
        #     left = 0
        #     right = len(s1) - 1
        #     while(left<right):
        #         temp = s1[left]
        #         s1[left] = s1[right]
        #         s1[right] = temp
        #         left +=1
        #         right -=1
        # reserve(s)
        # strg = s.split(" ")
        # result = ""
        # for i in range(len(strg)):
        #     reserve(strg[i])
        #     result+= i
        #     if i != len(strg)-1:
        #         result += " "
        # return result

        left, right = 0, len(s)-1
        while s[left] == " " and left <= right:
            left += 1

        while s[right] == " " and left <= right:
            right -= 1

        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right -1
        def reverse_each(l):
            start = end = 0
            while start < len(l):
                # go to the end of each word
                while end< len(l) and l[end] != " ":
                    end += 1
                
                reverse(l, start, end-1)

                start = end + 1
                end += 1
        reverse(output, 0, len(output)-1)
        reverse_each(output)

        return ''.join(output)

    # O(N)
    # O(N)
# @lc code=end


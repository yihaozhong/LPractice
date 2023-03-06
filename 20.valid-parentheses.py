#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def leftOf(self, char):
        if char == '}': return '{'
        elif char == ']': return '['
        else: return '('

    def isValid(self, s: str) -> bool:
        left = []
        for i in s:
            if i == '(' or i =='{' or i =='[':
                left.append(i)
            else:
                if left and self.leftOf(i) == left[-1]:
                    left.pop()
                else:
                    return False
        return not left
    
#  @lc code=end


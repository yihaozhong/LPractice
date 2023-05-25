#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # O(N) Time Complexity, we travese each char in string once, operations on stack takes O(1)
    # O(N) Space Complexity as we push all '(" in a stack at worst case
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


#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(start_index, path):
            if start_index == len(digits):
                result.append(''.join(path))
                return
            nextNumber = digits[start_index]
            for letter in KEYBOARD[nextNumber]:
                path.append(letter)
                dfs(start_index+1, path)
                path.pop()

        result = []
        if digits == "":
            return result
        dfs(0, [])
        return result
    
    # dfs -> backtesting
    
    """
    def dfs(index, path):
        if index == len(criteria):
            result.append(''.join(path))
        for child in node:
            path.append(child)
            dfs(index+1, path)
            path.pop()
    
    """

# @lc code=end

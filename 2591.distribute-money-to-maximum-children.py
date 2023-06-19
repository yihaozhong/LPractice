#
# @lc app=leetcode id=2591 lang=python3
#
# [2591] Distribute Money to Maximum Children
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # result = 0
        # if money < children:
        #     return -1
        # while children > 0:
        #     rest = money - 8
        #     if rest < 0:
        #         break
        #     if rest != 4:
        #         result += 1
        #     money -= 8
        #     children -= 1

        # return result

        money -= children
        print(money // 7)
        if money <0: return -1
        elif (money // 7 == children and money % 7 == 0):
            return children
        elif (money // 7 == (children - 1) and money % 7 == 3):
            return children - 2
        else:
            return min(children - 1, money // 7)
# @lc code=end


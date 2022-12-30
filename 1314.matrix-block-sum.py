#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # 1 2 3
        # 4 5 6
        # 7 8 9
        row = len(mat)
        col = len(mat[0])
        res = [[0] * (col) for _ in range(row)]
        preSum = [[0] * (col + 1) for _ in range(row + 1)]
        if row == 0 or col == 0:
            return None
        for i in range(1,row+1):
            for j in range(1, col+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + mat[i-1][j-1] - preSum[i-1][j-1]
        
        for i in range(row):
            for j in range(col):
                # top left corner
                x1 = max(i - k, 0)
                y1 = max(j - k, 0)

                # bottome right corner
                x2 = min(i+k, row - 1)
                y2 = min(j+k, col - 1)

                res[i][j] = preSum[x2+1][y2+1] - preSum[x1][y2+1] - preSum[x2+1][y1] + preSum[x1][y1]
        return res

    # Time: O(m*n), m is the number of rows, n is the number of columns of mat
    # Space: O(m*n)
# @lc code=end


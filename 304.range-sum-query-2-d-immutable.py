#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:
    preSum = None
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return None
        # create two d Array
        self.preSum = [[0]* (col + 1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                # cal the preSum [(0,0) (i,j)]
                self.preSum[i][j] = self.preSum[i - 1][j] + self.preSum[i][j-1] + matrix[i-1][j-1] - self.preSum[i-1][j-1]
        return None

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #print(self.preSum)
        return self.preSum[row2+1][col2+1] - self.preSum[row1][col2+1] - self.preSum[row2+1][col1] + self.preSum[row1][col1]


# Time - O(m * n) - for the constructor
# Space - O(m * n) - for storing the prefix sum array
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


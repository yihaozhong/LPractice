#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:

    # reverse a list
    def reverse(self, l):
        i, j=0, len(l)-1
        while (i< j):
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """

        # we swap the matrix
        # 1 2 3  1 4 7
        # 4 5 6  2 5 8
        # 7 8 9  3 6 9
        row = len(matrix)
        for i in range(row):
            for j in range(i, row):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for element in matrix:
            self.reverse(element)

    # O(N)
    # O(1)
    
# @lc code=end


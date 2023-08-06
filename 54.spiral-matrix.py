#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        visited = 101
        rows, columns = len(matrix), len(matrix[0])
        # four directions: right, down, left,up
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]

        current_direction = 0
        
        change_direction = 0
        # row is the row index; col is the column index, current index
        row = col = 0

        result = [matrix[0][0]]
        matrix[0][0] = visited

        while change_direction <2:
            while True:
                # calculate the next place we will move to
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # break if next step is out of bounds
                if not (0<= next_row< rows and 0 <= next_col < columns):
                    break
                # break if the next step is visted
                if matrix[next_row][next_col] == visited:
                    break
                # reset the chnage of direction
                change_direction = 0

                # update the cur position
                row, col = next_row, next_col

                result.append(matrix[row][col])
                matrix[row][col] = visited

            current_direction = (current_direction+1) %4
            change_direction += 1

        return result
# O(M*N)
# O(1)
#print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# revisit 8/6/2023
# @lc code=end


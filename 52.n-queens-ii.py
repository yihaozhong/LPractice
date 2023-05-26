#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    result = 0
    def totalNQueens(self, n: int) -> int:
        def isValid(board, row, col):
            # 检查列是否有皇后互相冲突
            for i in reversed(range(row)):
                    if board[i][col] == 'Q':
                        return False
            # 检查右上方是否有皇后冲突
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            # similarly
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            return True

        def backtracking(row, board):
            if row == n:
                self.result += 1
                return
            
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(row+1, board)
                board[row][col] = '.'

        empty_board = [["."] * n for _ in range(n)]
        
        backtracking(0, empty_board)
        return self.result
# @lc code=end


#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def isValid(board, row, col):
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
                result.append(create_board(board))
                #print(result)
                return
            
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(row+1, board)
                board[row][col] = '.'

        empty_board = [["."] * n for _ in range(n)]
        result = []
        backtracking(0, empty_board)
        return result
    
    # Time complexity: O(N!)
    # Space complexity: O(N^2)
# @lc code=end

# 36.Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # here we first define the hashset
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        # we run nested loop for fixed value so it will not run more then 81 times
        for r in range(9):
            for c in range(9):

                # if there is . then it is empty space we need to continue
                if board[r][c] == '.':
                    continue
                
                # Here we check if board value is exist in rows, cols or grid
                # if it is exist then it is duplicate which invalidate the sudoku
                # hence we'll return False
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in grid[r//3, c//3]
                ):
                    return False
                
                # Here we'll add board value to rows, cols and grid
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[r//3, c//3].add(board[r][c])

        # Once we loop through all the values in the loop and each values are valid
        # we'll return true
        return True

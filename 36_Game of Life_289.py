# 289. Game of Life
# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Truth table for this solution
        # Original  | New   | value
        # 0         |  0    |   0   : if current cell is 0 and neighbor != 3
        # 1         |  0    |   1   : if current cell is 1 and neighbor != [2,3]
        # 0         |  1    |   2   : if current cell is 0 and neighbor == 3
        # 1         |  1    |   3   : if current cell is 1 and neighbor == [2,3]

        #This will give you the count of rows and cols
        ROWS, COLS = len(board), len(board[0])

        # we'll create the helper funciton to count the neighbors
        def countneighbor(row, col):
            neighbor = 0
            # Here we're looping through neighbors
            # starting from top left to bottom right
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    # Here we're skipping if it is same cell
                    # if it is left  or top out of bound
                    # if it is right or bottom out of bound
                    if (r == row and c == col) or r < 0 or c < 0 or r == ROWS or c == COLS:
                        continue
                    # Here according to truth table if value is either 1 or 3 then that neighbor is 1(Alive)
                    # So, we'll update the neighbor
                    elif board[r][c] in [1,3]:
                        neighbor += 1
            return neighbor
        
        # here we're looping through each cell
        for r in range(ROWS):
            for c in range(COLS):

                # get the count of neighbors
                neighbor = countneighbor(r, c)

                # update the board as per the truth table
                if board[r][c]:
                    if neighbor in [2, 3]:
                        board[r][c] = 3
                else:
                    if neighbor == 3:
                        board[r][c] = 2

        # Again we're looping through each cell
        for r in range(ROWS):
            for c in range(COLS):
                # Update the board accoring to the truth table this time new state
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1


            
                    


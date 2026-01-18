# 74. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # First: We'll loop through entire matrix and if we found any value to zero we'll assign 
        # it's first row/col to 0. For the matrix[0][0] we'll utilize it for col so for row we'll use
        # extra variable
        first_row = False
        rows, cols = len(matrix), len(matrix[0])
        
        # loop through matrix
        for r in range(rows):
            for c in range(cols):
                # If any matrix value is 0
                if matrix[r][c] == 0:
                    # if it is first row 
                    if r == 0:
                        first_row = True
                        continue
                    # else we'll assign corresponding first row/col to 0
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # Second: We'll loop through matrix but this time skipping first row and col
        for r in range(1, rows):
            for c in range(1, cols):
                # If our memory row or col is 0 then we'll update the matrix value to 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # now if the first matrix (col memory) value is 0 then we'll update entire column to 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
            
        # If first row value (row memory) is 0 then we'll update entire row to 0
        if first_row:
            for c in range(cols):
                matrix[0][c] = 0
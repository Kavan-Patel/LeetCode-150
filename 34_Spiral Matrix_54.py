# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top, bottom = 0, len(matrix)
        right, left = len(matrix[0]), 0
        res = []
       
        while left < right and top < bottom:

            # First: Left --> Right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Second: Top --> Bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left< right and top < bottom):
                break

            # Third: Right --> Left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Forth: Bottom --> Top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
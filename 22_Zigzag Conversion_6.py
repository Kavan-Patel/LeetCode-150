# 6.Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1: return s
        # Result builder
        res = ""
        # Loop through given number of rows
        for r in range(numRows):
            # Increment for stright line, normal case
            increment = (numRows - 1) * 2
            # Loop in perticuler row until len of the string s
            # Here we user increment to jum through stright line
            for i in range(r, len(s), increment):
                # Append char to the string
                res += s[i]
                # Here we added zigzag line if there so we exclude first row 
                # and last row and add until end of row
                if (r > 0 and r < numRows - 1 and i + increment - (2 * r) < len(s)):
                    # If above conditions are true then it's a zigzag line
                    # We're adding that char to the result
                    res += s[i + increment - (2 * r)]
        # returning the result
        return res
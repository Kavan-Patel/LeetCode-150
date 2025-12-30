# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Here we first defind the counter
        count = 0 
        # loop through list but in reverse order
        for c in reversed(s):
            # if it is not empty space then increse the counter
            if c != ' ':
                count += 1
            # If it is empty space and counter is already incresed then 
            # return the counter
            # This will save an edge case like two or more space at the end
            # Since for initial space counter is not incresed.
            elif count > 0 and c == ' ':
                return count
        # return the counter again incase of empty string
        return count
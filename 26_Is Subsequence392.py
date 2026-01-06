# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Let's have substring pointer spoint
        spoint = 0

        # Handle edge case if substring is empty then return true 
        # because we can have empty substring from any string
        if len(s) == 0:
            return True
        
        # now loop through each char
        for c in t:
            # Check if char from t is matching with substring of spoint
            if s[spoint] == c:
                # If it does then increment spoint
                spoint += 1
            # If spoint is reach at the end of the len of sub string s then 
            # we can have substring and we can return true
            if spoint == len(s):
                return True
        # If we don't find any substring the return False
        return False


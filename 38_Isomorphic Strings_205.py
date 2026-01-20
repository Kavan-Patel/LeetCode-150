# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # First we'll define two hashmap mapping from s to t mapST
        # and mapping from t to s mapTS
        mapST, mapTS = {} , {}

        for i in range(len(s)):

            # Extract s char and t char
            cs = s[i]
            ct = t[i]

            # If any mapping exist (cs in mapST) and the new mapping 
            # we're trying to insert is not same as prioer mapping (mapST[cs] != ct)
            # Then return False
            if ( (cs in mapST and mapST[cs] != ct) or
                (ct in mapTS and mapTS[ct] != cs)):
                return False

            # mapping from s to t
            mapST[cs] = ct
            # mapping from t to s
            mapTS[ct] = cs

        return True
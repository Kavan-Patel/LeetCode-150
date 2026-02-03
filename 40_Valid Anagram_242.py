# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Assign two builder hashmap
        sMap, tMap = {}, {}

        # Build hashmap for s
        for i in range(len(s)):
            schar = s[i]
            if schar in sMap:
                sMap[schar] += 1
            else:
                sMap[schar] = 1
        # Build hashmap for t
        for j in range(len(t)):
            tchar = t[j]
            if tchar in tMap:
                tMap[tchar] += 1
            else:
                tMap[tchar] = 1
        
        return True if sMap == tMap else False


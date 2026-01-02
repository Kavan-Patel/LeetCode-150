# 28.Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Loop until the variable which is needle space away from last position
        hayLen = len(haystack)
        needLen = len(needle)
        for i in range(hayLen - needLen + 1):
            # here slice haystack starting from ith variable to the len of needle
            # which gives you same len word like needle which we can compare it with needle
            if haystack[i : i + needLen] == needle:
                # If we find any similar word then we'll return position i
                return i
        # else we'll return -1
        return -1
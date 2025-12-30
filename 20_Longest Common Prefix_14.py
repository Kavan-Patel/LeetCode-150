# 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # First we sort the list to avaoid edge case like ['aa','a','aa']
        # By sorting we'll get ['a','aa','aa']
        strs.sort()

        # Then we grab the first and last list 
        # in our example first = 'a' and last ='aa'
        first = strs[0]
        last = strs[-1]
        # created empty res
        res = ''

        # loop through min of first or last list
        for i in range(min(len(first), len(last))):
            # if latter is different then we're returning the result
            if first[i] != last[i]:
                return res
            # else we're adding that latter to the result
            res += first[i]
        # return the result
        return res

                
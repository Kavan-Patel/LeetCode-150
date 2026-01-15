# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

# Pseudo Code
#### Sliding Window ####
# 1. We'll use set data structure as it does not contain any duplicate
#     initialize left index as 0
# 2. run loop and get each char one by one 
# 3. run another while loop which checks if char in our set then 
#     remove one char from left and increse the left index
# 4. if char is not present in SET then add that char in set
# 5. set result as max of existing results and r - l + 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, res = 0, 0
        res_set = set()

        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1
            res_set.add(s[r])
            res = max(res, r-l+1)
        return res

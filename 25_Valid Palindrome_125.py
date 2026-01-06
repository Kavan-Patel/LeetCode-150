# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # let's define result 
        res = ''

        # now let's take each char and check if it is alpha numeric by using python's inbuilt
        # function isalnum()
        for c in s:
            if c.isalnum():
                # now that we have valid alphanumeric char 
                # we wanted to convert it to lower case and add it to the result
                res += c.lower()
        
        # now we check if result and reverse of result is true, if it is then we'll return the result
        return True if res == res[::-1] else False
        
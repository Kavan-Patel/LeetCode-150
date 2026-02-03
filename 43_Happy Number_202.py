# 202.Happy Number
# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isHappy(self, n: int) -> bool:
        
        # Here first we'll define the hash set
        visit = set()

        # we're checking if the given number is in the set 
        # if it is then it is repeting the pattern and we'll return the false
        while n not in visit:
            # If it is not in the set then we'll add that number
            visit.add(n)

            # we'll create the helper function to get the square of numbers
            n = self.squareOfNumbers(n)
            # if we ever reach to 1 then number is happy we'll return true
            if n == 1:
                return True

        return False
    def squareOfNumbers(self, n: int) -> int:
        # squared sum output
        output = 0 
        
        # while n is not 0
        while n:
            # this takeout last digit
            digit = n % 10
            # we'll do the square of the digit
            digit = digit ** 2
            # add that digit in the output
            output += digit
            # and update the digit by removing the last one
            n = n // 10
        #return the output
        return output

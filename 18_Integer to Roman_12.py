# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def intToRoman(self, num: int) -> str:
        # Here we created Nested List with symbol and value, also include special case
        # and arrange list in reversed order
        romanList = [
            ['M', 1000], ['CM', 900],
            ['D',500] ,['CD',400],
            ['C',100] ,['XC',90],
            ['L',50] ,['XL',40],
            ['X',10] ,['IX',9],
            ['V',5] ,['IV',4],
            ['I',1]
        ]
        # define the empty result
        res = '' 
        # run loop until romanList
        for sym, val in romanList:
            # if first number is available for ex 476 // 400 = 1 then it goes inside
            # if first number is not available for ex 476 // 1000 = 0 then it will ignore
            if num // val:
                # Here it got the count
                count = num // val
                # Multiply that count with symbole and added it result 
                res = res + (count * sym)
                # update the number for next iteration
                # for ex 476 % 400 = 76
                num = num % val
        # return the result
        return res

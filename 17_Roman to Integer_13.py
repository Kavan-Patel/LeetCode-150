# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        # Here let's assign romanMap as given in the question to the Hashmap
        romanMap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        # Assign total_sum and prev_val to 0
        total_sum = 0
        prev_val = 0

        # Here we're reversed the input and loop it to extract char in c
        for c in reversed(s):
            # Retrive current_val from map
            current_val = romanMap[c]

            # current val should be bigger in ideal case since we reversed the string
            # if it is not bigger then we substract it which take care of 6 exceptions given in the question
            if current_val < prev_val:
                total_sum -= current_val
            # if it is bigger then we add it to the total
            else:
                total_sum += current_val
            # Don't forgot to change prev_val to current_val for next iteration
            prev_val = current_val
        # return total_sum
        return total_sum
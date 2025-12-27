# 135.Candy
# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Here if we go with nested loop bruteforce approch then time complexity is O(n^2)
        # So we'll use two pass approch

        # First we'll address first condition which is 1 must assign 1 candy to each child
        assignments = [1] * len(ratings)

        # First we'll check current value with left neighbour and update the current assignment
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                # To update assignment we'll take left neighbour and add 1 to it and assign it to
                # current value
                assignments[i] = assignments[i-1] + 1
        
        # Then we'll check current value with right neighbour and update the current assignment 
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Here since all values of assignments are not 1 so We'll take right neighbour value 
                # add one to it and takeout max value of current and our calculation
                assignments[i] = max(assignments[i], assignments[i + 1] + 1)
        # Return sum of total assignments
        return sum(assignments)
                
                
       
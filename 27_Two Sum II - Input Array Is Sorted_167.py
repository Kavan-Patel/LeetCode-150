# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Here we'll use two pointer approach 
        l, r = 0, len(numbers) - 1 

        # We're looping until l pointer does not meet r pointer 
        while l < r:
            # Adding first and last element of the list
            total_sum = numbers[l] + numbers[r]

            # Since numbers are in non decresing order We'll check it with the result 
            # If total sum is greater then the target then we need to reduce right index
            if target < total_sum:
                r -= 1
            # If total sum is less then the target then we need to increse the left index
            elif target > total_sum:
                l += 1
            # Else target and total sum will be the same and we got the indices
            else:
                # We'll increse left and right to one indices as list start from 0
                return [l+1, r+1]
        


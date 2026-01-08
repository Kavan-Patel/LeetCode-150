# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Here we'll use sliding window approch
        # first we'll start left and right pointer from 0
        l , r = 0, 0
        currentSum =0 
        res = float('inf')

        # We'll run the loop until all the nums
        while r < len(nums):
            # Add all new num to currentSum
            currentSum += nums[r]
            # if currentSum reaches to grater or equal to target
            while currentSum >= target:
                # we'll get min len
                res = min(res, r - l + 1)
                # We'll reduce left number and pointer and calculate current sum again
                currentSum -= nums[l]
                l += 1
            # Increment for outer while loop
            r += 1
        # Here we'll return 0 if res is same as declared one
        return 0 if res == float('inf') else res


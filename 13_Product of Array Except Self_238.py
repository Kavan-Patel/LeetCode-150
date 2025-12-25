# 238.Product of Array Except Self

# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       # Here we can calculate prefix and postfix first
       # for ex [1,2,3,4]. [1,1,1,1]
       # prefix  [1,1,2,6] 
       # postfix [24,12,4,1]
       # res [prefix * postfix] = [24,12,8,6]

        res = len(nums) * [1]

        # prefix loop
        for i in range(1, len(nums)):
            # Here we start with the index 1 as for the prefix first index is always 1
            # we multiply previous res with previous number
            res[i] = res[i-1] * nums[i-1]
        
        # postfix loop
        postfix = 1
        for j in range(len(nums)-2, -1, -1):
            # We calculate postfix in reverse manner and also multiply it with our previous prefix
            # Here skipping last index as postfix for last index is always 1
            postfix = postfix * nums[j+1]
            res[j] = res[j] * postfix

        return res

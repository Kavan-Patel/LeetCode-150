# 189. Rotate Array

# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This make sure if k is larger then len of the list then it will bring
        # down to the len of list
        k = k % len(nums)
        # this make sure of edge case 
        if len(nums) > 1:            
            # First we reverse the list which takes O(n) time and O(1) as
            # in place list reversal happen in python
            nums.reverse()

            # Let's consider to reverse 2nd half so starting from k  to len
            l = k
            r = len(nums) - 1
            while l < r:
                nums[l], nums[r]  = nums[r], nums[l]
                l += 1
                r -= 1
            
            # now let's reverse the first part of the list
            l = 0
            r = k - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        


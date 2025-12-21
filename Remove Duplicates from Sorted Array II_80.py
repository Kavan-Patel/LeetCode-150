# 80. Remove Duplicates from Sorted Array II

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Edge case
        if len(nums) <= 2:
            return len(nums)
        
        # Two pointer approch 
        w = 2

        for r in range(2, len(nums)):
            # it check if 2 point back if value is same then it do nothing
            # if value is different then we replace the Running pointer r with 
            # write pointer w
            if nums[r] != nums[w - 2]:
                nums[w] = nums[r]
                w += 1
        return w

        


    
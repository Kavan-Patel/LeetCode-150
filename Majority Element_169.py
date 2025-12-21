# 169. Majority Element

# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # # two line solution
        # nums.sort()
        # # Since we're sorting the list majority of element should be in the middle
        # return nums[len(nums) // 2]
        
        # With boyer moore Voting Algorithm time O(n) space O(1)
        candidate = 0
        count = 0

        for num in nums:
            # This will help changing candidate 
            if count == 0:
                candidate = num
            
            if num != candidate:
                count -= 1
            else:
                count += 1
        return candidate
            
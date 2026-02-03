# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return [i, seen[nums[i]]]
            seen[target - nums[i]] = i

# Time complexity is O(n) as we loop through list one time 
# Hashing is having time complexity of O(1)

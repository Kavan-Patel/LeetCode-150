# 55 Jump Game

# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Working from backward
        # First set the goal which is last number in the nums
        goal = len(nums) - 1
        
        # loop it backward
        for i in range(len(nums)-1, -1, -1):
            # if goal is reachable from the current number then
            # set the current indices to the goal 
            if i + nums[i] >= goal:
                goal = i
        
        # Since we're updating the goal it should reach to the start
        # position if not we endup returning the False
        return True if goal == 0 else False
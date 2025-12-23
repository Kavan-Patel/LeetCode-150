# 45 Jump Game II

# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # First initialize result
        res = 0 
        # set window variable left and right initially 0
        l = r = 0

        # Run the loop until right window hits the goal
        while r < len(nums)-1:

            farthest = 0
            # Loop though window and find farthest point
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            # update new window
            l = r + 1
            r = farthest
            # update the result
            res += 1
        return res
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def trap(self, height: List[int]) -> int:

        # Here we'll user two pointer approch
        # first assign lefft pointer to the first index and right to last index
        l, r = 0, len(height) - 1
        # Let's assume maxLeft and maxRight are value at l and r
        maxLeft, maxRight = height[l], height[r]
        # Initialize trapped water with 0 value
        trappedWater = 0

        # Here we loop it until left index is smaller then right index
        while l < r:
            # if leftMax is smaller or equal to the maxRight
            if maxLeft <= maxRight:
                # Here we increse the left pointer and calculate trapped water 
                # to calculate we substract current height with leftMax
                # If it is negetive then we ignore and update the maxLeft
                # if it is positive then add the difference to trappedWater and upate maxLeft
                l += 1
                if maxLeft - height[l] > 0:
                    trappedWater += (maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                
            # if rightMax is smaller then leftMax
            else:
                # We'll do the same for right pointer like we did for left pointer
                r -= 1
                if maxRight - height[r] > 0:
                    trappedWater += (maxRight - height[r])
                maxRight = max(maxRight, height[r])
        return trappedWater
















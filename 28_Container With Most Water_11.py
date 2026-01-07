# 11. Container With Most Water

# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Here we'll use two pointer approch at the start and end
        l , r = 0, len(height) - 1
        # Let's define water storage and initial space between first and last
        storage = 0
        space = len(height) - 1

        # Loop until l and r meet
        while l < r:
            # Update the storage, maximum of existing storage and the new calculation
            storage = max(storage, min(height[l], height[r]) * space)

            # Here if left height is less then we'll increse left pointer
            if height[l] < height[r]:
                l += 1
            # IF right height is less then we'll decrese right pointer
            else:
                r -= 1

            # Decresing the space by one as we iterate through loop
            space -= 1
        # Return the water storage
        return storage


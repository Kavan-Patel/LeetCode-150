# 219.Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # First we'll define the left pointer and the window set
        L = 0
        window = set()

        # loop through list
        for R in range(len(nums)):
            # if R - L > k then we have to shrink the window from left
            if R - L > k:
                window.remove(nums[L])
                L += 1
            # we'll check if right element is exist in the window
            # if it does then we found the duplicate and return true
            if nums[R] in window:
                return True

            # at the end we're adding the right pointer element to the window
            window.add(nums[R])
        # If we don't find any duplicate then we'll return False
        return False
# 27. Remove Element

# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        

        # Assign two pointer at the end
        i, e = len(nums) - 1, len(nums) - 1

        # Loop until end of the array if it equals to value then move that number
        # at the end with the help of e(end tracker)
        while i >= 0:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[e]
                nums[e] = temp
                e -= 1
                i -= 1
            else:
                i -= 1
        
        return e + 1
            


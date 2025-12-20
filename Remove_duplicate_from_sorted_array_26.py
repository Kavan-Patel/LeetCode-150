# 26. Remove Duplicates from Sorted Array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointer approch
        i, j = 0, 1

        # Check if fast moving pointer does not cross total length of array
        while j <= len(nums) - 1:
            # if same number encounter move j faster until unique number found
            if nums[i] == nums[j]:
                j += 1
            else:
                # if unique found then swap it with next
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                # Don't forgot to move fast pointer as well
                j += 1
        # Important: Don't forgot to add 1 as i start at 0th index 
        # and length of the array should consider from 1
        return i + 1
                
        
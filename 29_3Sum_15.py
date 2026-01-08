# 15. 3Sum
# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Here we'll use two sum problem with Pivot to solve threeSum
        # Declare the res and sort the nums (Sorting will take N log n time complexity)
        res = []
        nums.sort()

        # We run the loop through list to get the pivot one by one
        for i in range(len(nums)):

            # If pivot i is at 2nd or grater positionn 
            # and same as previous then we'll skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Now we'll assign l and r and solve it like two sum
            l , r = i+1, len(nums) -1 
            while l < r:
                # Add all the number
                threeSum = nums[i] + nums[l] + nums[r]
                # if it is < 0 then we'll increse the left pointer to increse the sum
                if threeSum < 0:
                    l += 1
                # if it is > 0 then we'll decrese the right pointer to decrese the sum
                elif threeSum > 0:
                    r -= 1
                # If it is 0 then we'll append the result
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # now after incresing the left pointer we'll compare it with previous 
                    # pointer, if both are the same then we may skip the pivot as it will
                    # give the same results as previous 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
# 274. H-Index
# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # First we sort the list descending, it took O(n log n)
        citations.sort(reverse=True)
        # Counter to find max H index
        hindex = 0
        for i in range(len(citations)):
            # Here we check if citation for current number is same or bigger then 
            # index then it setisfy the H index defination. We break the loop if 
            # condition is not setisfied
            # [1,3,1] --> First sorting in descending [3,1,1]
            # now for 3 we have atlist 1 citation
            # for 1 we don't have atlist 2 citation
            # for 1 we don't have atlist 3 citation
            if citations[i] >= i+1:
                hindex += 1
            else:
                break
        return hindex
# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # One line solution Complexity O(N + M)
        #return Counter(ransomNote) <= Counter(magazine)
        
        magazineMap = defaultdict(int)
        for char in magazine:
            magazineMap[char] += 1
        
        for char in ransomNote:
            if magazineMap[char] > 0:
                magazineMap[char] -= 1
            else:
                return False
        return True

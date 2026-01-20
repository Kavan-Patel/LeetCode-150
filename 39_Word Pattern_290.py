# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # This will split the line in words and store it in list
        words = s.split()

        # Edge case if length are not equal
        if len(pattern) != len(words):
            return False

        # Here we're using charMap to store mapping char to word
        # and usedWord set to check if same word comes again that violate the rules
        charMap = {}
        usedWord = set()
        
        # Looping through the len
        for i in range(len(pattern)):
            
            char = pattern[i]
            if char in charMap:
                if charMap[char] != words[i]:
                    return False
            else: 
                if words[i] in usedWord:
                    return False
                usedWord.add(words[i])
                charMap[char] = words[i]
        return True
        

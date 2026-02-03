# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
# Counting complexity can be tricky
# n number of string
# k size of each string
# k log k to sort the string
# n we're doing it for n times
# O(n * k log k)
# n for returning n values : we can negligate this 
# Space complexity is n k

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Here first we define hash map wich has values as list
        anaMap = defaultdict(list)
        # Looping through the strs
        for word in strs:
            # We're creating charKey of 26 value list each is 0 initially
            charKey = [0] * 26
            # Looping through each word
            for c in word:
                # Here we're substracting char with a to get it's position and increse position by one
                charKey[ord(c)- ord('a')] += 1
            # Here we're converting charKey list to tuple (because tuples are immutable ordered list)
            # we'll append each word to charKey
            anaMap[tuple(charKey)].append(word)
        # return all the values of the map and convert it to the list 
        return list(anaMap.values())


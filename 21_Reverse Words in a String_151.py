# 151.Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        # First defind two empty string one is to store result and one is for temp string
        res = ''
        temp = ''
        # loop through s
        for i, c in enumerate(s):
            # Word building, if no space then build word in temp
            if c != ' ':
                temp += c
            # if there's space or end of the sentence and temp is having word
            # then add it to result in reverse order
            if (c == ' ' or i == len(s)-1) and len(temp) > 0:
                # if it is the first word
                if len(res) == 0:
                    res = temp
                # else we'll keep the space in between
                else:
                    res =  temp + ' ' + res
                temp = ''
        # return the result
        return res
            
        # # Python way

        # return " ".join(s.split()[::-1])
        # # here .split(). split the string by words by removing all the space, 
        # # even leading and trailing space
        # # [::-1] reversed the splitted words
        # # " ".join(). will join those word by one space
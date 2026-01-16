# 76.Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) == 0:
            return ""
        
        # Declaring variables
        tmap, window = {}, {}
        res, resLen = [-1, -1], float('infinity')
        
        # building tmap
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        
        have, need = 0, len(tmap)
        l = 0

        for r in range(len(s)):

            # initialize window
            window[s[r]] = 1 + window.get(s[r], 0)

            # Update have variable
            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
            
            while have == need:
                # now popoing from left
                window[s[l]] -= 1

                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                
                # Check if this window is smaller then the resLen
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                l += 1
        # we need to unpack l, r
        l, r = res
        # return s[l, r+1] if resLen changed from infinity
        return s[l: r+1] if resLen != float('infinity') else ""

        

        
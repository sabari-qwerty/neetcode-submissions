class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        see = set()

        maxLength = 0 

        l = 0 
        r = 0 

        n = len(s)

        while r < n: 

            while s[r] in see: 
                see.remove(s[l])
                l += 1
                
            see.add(s[r])

            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength


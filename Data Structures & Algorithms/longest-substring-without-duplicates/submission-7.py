class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        see = set()

        l = r = 0 

        n = len(s)

        maxLength = 0 

        while r < n: 

            while s[r] in see: 
                see.remove(s[l])
                l += 1

            maxLength = max(maxLength, r - l + 1)
            see.add(s[r])

            r += 1

        return maxLength

            
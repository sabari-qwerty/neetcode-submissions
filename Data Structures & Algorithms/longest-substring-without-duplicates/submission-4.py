class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        see = set()

        n = len(s)

        l = 0 

        maxLength = 0 

        for r in range(n): 


            while l < r and s[r] in see: 
                see.remove(s[l])
                l += 1

            see.add(s[r])

            maxLength = max(len(see), maxLength)

        return maxLength

        


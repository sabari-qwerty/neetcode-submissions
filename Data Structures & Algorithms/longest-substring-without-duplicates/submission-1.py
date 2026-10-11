class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        l = 0
        r = 0

        window = set()

        ans = 0 


        while r < n: 

            while s[r] in window: 

                window.remove(s[l])
                l += 1

            #  extend 
            window.add(s[r])

            ans = max(ans, r - l + 1)

            r += 1

        return ans


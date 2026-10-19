class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window = {}

        ans = 0 

        l = 0 

        maxFreq = 0



        n = len(s)

        for r in range(n):

            window[s[r]] = window.get(s[r], 0) + 1

            maxFreq = max(window[s[r]], maxFreq)


            while r - l + 1 - maxFreq > k:

                window[s[l]] -= 1 

                l += 1

            ans = max(ans, r - l + 1)

        return ans
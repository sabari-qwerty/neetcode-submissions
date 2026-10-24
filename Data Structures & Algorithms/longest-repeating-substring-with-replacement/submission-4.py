class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window = {}

        l = 0 
        maxFreq = 0
        ans = 0 

        for r in range(len(s)): 

            window[s[r]] = window.get(s[r], 0) +1

            maxFreq = max(window[s[r]], maxFreq)

            while (r - l + 1) - maxFreq > k: 
                window[s[l]] -=  1
                l += 1

            ans = max(r - l +1, ans)

        return ans



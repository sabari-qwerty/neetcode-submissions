class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        l = 0 
        maxFreq = 0 
        ans = 0 
        count = {}

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(count[s[r]], maxFreq)

            while (r  - l + 1) - maxFreq > k: 
                count[s[l]] -= 1
                l += 1

            ans = max(r - l + 1, ans)

        return ans

         


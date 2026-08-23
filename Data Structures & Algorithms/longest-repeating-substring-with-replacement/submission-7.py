class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0 

        maxF = 0
        l =  0
        n = len(s)

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(count[s[r]], maxF)

            while (r - l + 1) - maxF > k:

                count[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)

        return res 

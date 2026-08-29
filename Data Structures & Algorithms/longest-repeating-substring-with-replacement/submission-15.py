class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        ans = 0
        count, maxFreq = {}, 0 

        l = 0

        for r in range(n):
            key = s[r]
            count[key] = count.get(key, 0) + 1
            maxFreq = max(maxFreq, count[key])

            while (r - l + 1) -  maxFreq  > k:

                count[s[l]] -= 1

                l += 1
            ans = max(r - l + 1, ans)

        return ans 
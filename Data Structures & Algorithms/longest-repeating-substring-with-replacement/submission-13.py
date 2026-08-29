class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        count = {}

        maxFreq = 0 

        ans = 0 

        l = 0 


        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])


            while (r - l + 1) - maxFreq > k: 
                 count[s[l]] -= 1
                 l += 1

            ans = max(r - l + 1, ans)


        return ans 
        
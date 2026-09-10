class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        count = {}


        l = 0 
        

        maxLength = 0

        n = len(s)

        ans = 0


        for r in range(n):

            key = s[r]

            count[key] = count.get(key, 0) + 1

            maxLength = max(maxLength, count[key])



            while (r - l + 1) - maxLength > k:

                key = s[l]

                count[key] -= 1

                l += 1   

            ans = max(r - l + 1, ans)


        return ans


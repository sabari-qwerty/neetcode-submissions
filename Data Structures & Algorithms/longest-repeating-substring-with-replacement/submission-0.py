class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_repeting = 0 

        char_count = {}

        l = r = 0 

        n = len(s)

        maxf = 0

        res = 0

        while r < n:

            char_count[s[r]] = char_count.get(s[r], 0) + 1

            maxf = max(char_count[s[r]], maxf)

           
            while (r - l + 1 ) - maxf > k: 

                char_count[s[l]] -= 1

                l += 1

            res = max(res, r - l +1)

            r += 1


        return res
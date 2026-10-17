class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for char in t: 
            t_count[char] = t_count.get(char, 0)+1

        min_length = float('inf')
        res = ""

        count = 0 

        l = r = 0 

        n = len(s)

        window = {}

        while r < n: 

            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in t_count and  t_count[s[r]] == window[s[r]]:
                count += 1

            while count == len(t_count):


                if r -l + 1 < min_length:
                    res = s[l:r+1]
                    min_length = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in t_count and t_count[s[l]] > window[s[l]]:
                    count -= 1


                l += 1

            r += 1

        return res
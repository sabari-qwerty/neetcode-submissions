class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for i in t: 
            t_count[i] = t_count.get(i, 0) + 1

        ans = ""
        
        l = 0
        maxLengt = float('inf')
        window = {}
        count = 0 

        for r in range(0, len(s)):

            key = s[r]

            window[key] = window.get(key, 0) + 1

            if key in t_count and t_count[key] == window[key]: 
                count += 1

            while count == len(t_count): 

                if maxLengt > r - l + 1: 
                    maxLengt = r - l + 1
                    ans = s[l:r+1]

                key = s[l]

                window[key] -= 1

                if key in t_count and t_count[key] > window[key]:
                    count -= 1

                l += 1
        return ans

 





class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for i in t: 
            t_count[i] = t_count.get(i, 0) + 1

        s_count = {}
        ans = ""
        minLength = float('inf')

        count = 0 

        l = 0 

        for r in range(len(s)):

            key = s[r]

            s_count[key] = s_count.get(key, 0) + 1

            if key in t_count and t_count[key] == s_count[key]:
                count += 1

            while count == len(t_count): 

                if r - l + 1 < minLength: 
                    minLength = r - l + 1
                    ans = s[l:r+1]

                key = s[l]

                s_count[key] -= 1

                if key in t_count and t_count[key] > s_count[key]:
                    count -= 1


                l += 1

        
        return ans
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for i in t: 
            t_count[i] = t_count.get(i, 0) + 1

        count = 0 

        s_count = {}
        ans = ""
        l = 0 

        min_length = float('inf')

        for r in range(len(s)):

            key = s[r] 

            s_count[key] = s_count.get(key, 0) + 1

            if key in t_count and  t_count[key] == s_count[key]: 
                count += 1

            while count == len(t_count):

                if r - l + 1 < min_length: 
                    min_length = r - l + 1
                    ans = s[l:r+1]


                key = s[l]

                s_count[key] -= 1


                if key in t_count and t_count[key] > s_count[key]: 
                    count -= 1

                l += 1

        return ans

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for i in t: 
            t_count[i] = t_count.get(i, 0) + 1

        ans = ""
        minCount = float('inf') 

        l = 0 

        window = {}

        have = len(t_count)
        need = 0 

        for r in range(len(s)): 

            key = s[r]

            window[key] = window.get(key, 0) + 1

            if key in t_count and t_count[key] == window[key]: 
                need += 1


            while have == need:

                key = s[l]
                window[key] -= 1

                length = r - l + 1

                if minCount > length : 

                    minCount = length
                    ans = s[l:r+1]


                if key in t_count and t_count[key] > window[key]: 
                    need -= 1


                l += 1

        return ans
     


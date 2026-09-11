class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_count = {}

        for i in t:

            t_count[i] = t_count.get(i, 0) + 1

        start = 0 
        end = 0 
        have = 0 
        need = len(t_count)
        n = len(s)
        window = {}
        length = float('inf') 
        l = 0

        for r in range(n): 
            key = s[r]
            window[key] = window.get(key, 0) + 1

            if key in t_count and window[key] == t_count[key]: 
                have += 1

            while have == need:

                if r - l + 1 < length: 
                    start = l
                    end = r + 1
                    length = r - l + 1

                key = s[l]
                window[key] -= 1

                if key in t_count and window[key] < t_count[key]: 
                    have -= 1

                l += 1

        if length == float('inf'): return ""

        return s[start:end]


 

            
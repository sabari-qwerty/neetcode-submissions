class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_of_t = {}

        for key in t:
            count_of_t[key] = count_of_t.get(key, 0) + 1

        window = {}
        start = -1 
        end = -1
        length = float('inf')
        l = 0 
        have = 0 
        need = len(count_of_t)

        for r in range(len(s)): 
            key = s[r]
            window[key] = window.get(key, 0) + 1

            if key in count_of_t and count_of_t[key] == window[key]: 
                have += 1

            while have == need:

                if r - l + 1 < length:
                    start = l 
                    end = r + 1
                    length = r - l + 1

                key = s[l]
                window[key] -= 1

                if key in count_of_t and count_of_t[key] > window[key]: 
                    have -= 1
                l += 1

        if length == float('inf'): return ""

        return s[start:end]

                

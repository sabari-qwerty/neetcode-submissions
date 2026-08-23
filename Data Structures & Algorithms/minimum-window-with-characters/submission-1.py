class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_of_t = {}

        for i in t:
            count_of_t[i] = count_of_t.get(i, 0) + 1

        window = {}
        have = 0 
        need = len(count_of_t)
        start = -1
        end = -1
        l = 0 
        length = float('inf')

        for r in range(len(s)): 
            
            char = s[r]

            window[s[r]] = 1 + window.get(s[r], 0) 

            if char in count_of_t and count_of_t[char] == window[char]: 
                have += 1

            while have == need: 
                if r - l + 1 < length:
                    start = l 
                    end = r
                    length = r - l + 1

                window[s[l]] -= 1

                if s[l] in count_of_t and count_of_t[s[l]] > window[s[l]]: 
                    have -=1 
                l += 1

        if length == float('inf'): return ""

        return s[start:end+1]

             



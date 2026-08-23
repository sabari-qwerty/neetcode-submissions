class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT = {}
        window = {}
        start = - 1
        end = -1

        for i in t: 
            countT[i] = countT.get(i, 0) + 1

        have = 0 
        need = len(countT)

        minLength = float('inf')

        #  windows starting
        l = 0 

        for r in range(len(s)): 

            char = s[r]

            # grow the window 
            window[char] = window.get(char, 0) + 1

            if char in countT and countT[char] == window[char]: 
                have += 1

            while have == need:

                if r - l  + 1 < minLength:
                    start = l 
                    end = r
                    minLength = r - l + 1

                window[s[l]] -= 1

                if s[l] in countT and countT[s[l]] > window[s[l]]: 
                    have -= 1

                l += 1

        if minLength == float('inf'): return ""

        return s[start:end+1]
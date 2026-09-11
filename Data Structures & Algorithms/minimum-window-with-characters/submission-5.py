class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}
        
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1

        have = len(t_count)
        need = 0 
        start = 0 
        end = 0 
        length = float('inf')
        window = {}
        l = 0 

        for r in range(len(s)): 

            # grow logic
            key = s[r]
            window[key] = window.get(key, 0) + 1

            if key in t_count and t_count[key] == window[key]: 
                need += 1


            # shrink logic
            while need == have: 

                if r - l + 1 <  length:
                    start = l 
                    end = r 
                    length = r - l + 1


                key = s[l]
                window[key] -= 1


                if key in t_count and t_count[key] > window[key]: 
                    
                    need -= 1

                l += 1

        if float('inf') == length: return ''

        return s[start:end+1]







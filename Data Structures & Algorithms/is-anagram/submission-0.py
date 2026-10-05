class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        freq = [0] * 26 

        for i in range(len(s)):

            a_ascii_value = ord('a') 

            s_idx =  ord(s[i]) - a_ascii_value
            t_idx = ord(t[i]) - a_ascii_value

            freq[s_idx] += 1 
            freq[t_idx] -= 1

        for i in freq: 

            if i != 0: return False

        return True

        


        
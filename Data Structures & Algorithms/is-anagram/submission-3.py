class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        freq = [0] * 26

        for idx in range(len(s)):

            a = ord('a') 

            s_idx = ord(s[idx]) - a
            t_idx = ord(t[idx]) - a

            freq[s_idx] += 1
            freq[t_idx] -= 1

        for i in freq: 
            if i != 0: return False

        return True
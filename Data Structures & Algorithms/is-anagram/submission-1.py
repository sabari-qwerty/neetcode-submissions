class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        freq = [0] * 26

        n = len(s)

        for i in range(n):
            
            diff_s = ord(s[i]) - ord('a')

            diff_t = ord(t[i]) - ord('a')

            freq[diff_s] += 1
            freq[diff_t] -= 1

        for i in freq: 

            if i != 0: return False


        return True
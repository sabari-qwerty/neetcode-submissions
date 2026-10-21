class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        n = len(s)

        array = [0] * 26

        for i in range(n):

            a_asii_idx = ord('a')

            array[ord(s[i]) - a_asii_idx ] += 1
            array[ord(t[i]) - a_asii_idx ] -= 1

        for i in array: 
            if i != 0: return False

        return True
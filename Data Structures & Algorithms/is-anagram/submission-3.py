class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        fre_map = [0] * 26

        for i in range(len(s)):
            fre_map[ord('a') - ord(s[i])] += 1
            fre_map[ord('a') - ord(t[i])] -= 1

        for i in fre_map: 
            if i != 0: return False

        return True

            


            



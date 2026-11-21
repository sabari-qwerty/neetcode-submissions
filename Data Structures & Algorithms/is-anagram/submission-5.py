class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ans = [0] * 26 

        if len(s) != len(t): return False

        for i in range(len(s)):

            a = ord('a')


            idx =   ord(s[i]) - a
            ans[idx] += 1
            idx =ord(t[i]) - a
            ans[idx] -= 1

        for i in ans: 

            if i != 0: return False

        return True

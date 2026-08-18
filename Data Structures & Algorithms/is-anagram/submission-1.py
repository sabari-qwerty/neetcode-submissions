class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        ans = [0] * 27 

        for i in s:
            idx = ord(i) - ord('a') 
            ans[idx] += 1

        for i in t: 
            idx = ord(i) - ord('a') 
            ans[idx] -= 1

        print(ans)

        for i in ans:
            if i != 0: return False

        return True 

          
class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        n = len(s)

        l = 0 
        r = n -1

        while l < r: 

            while  0 <= r and  not s[r].isalnum(): r -=1
            while l < n  and not s[l].isalnum(): l +=1

            if r < l: return True

            if s[l].lower() != s[r].lower(): return False

            l += 1
            r -=1

        return True




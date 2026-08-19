class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower_case = s.lower()

        n = len(s)

        l = 0 
        r = n -1

        while l < r: 

            while  0 <= r and  not lower_case[r].isalnum(): r -=1
            while l < n  and not lower_case[l].isalnum(): l +=1

            if r < l: return True

            if lower_case[l] != lower_case[r]: return False

            l += 1
            r -=1

        return True




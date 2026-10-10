class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""

        for char in strs:

            ans += str(len(char)) + "#" + char

        return ans 

    def decode(self, s: str) -> List[str]:

        ans = []

        l = 0 
        r = 0

        n = len(s) 

        while r < n: 

            while s[r] != '#': 
                r += 1

            count = int(s[l:r])
            l = r +1 
            r = l+count

            ans.append(s[l:r])

            l = r
            r += 1

             


        return ans

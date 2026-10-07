class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""

        for char in strs: 

            string += str(len(char)) + "#" + char

        return string 


    def decode(self, s: str) -> List[str]:

        ans = []

        l = 0 
        r = 0 

        n = len(s)

        while r < n:

            while r < n and s[r] != "#" : 

                r += 1 

            count = int(s[l:r])


            l = r + 1
            r = l + count

            ans.append(s[l:r])

            l = r             

        return ans

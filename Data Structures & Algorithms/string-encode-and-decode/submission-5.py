class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for i in strs: 

            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:

        l, r = 0, 0 

        n = len(s)

        ans = []


        while r < n: 

            while s[r] != "#": 
                r += 1

            print(s[l:r])

            length = int(s[l:r])

            l = r + 1

            ans.append(s[l:l + length ])

            r += length + 1
            l = r


        return ans






        return []



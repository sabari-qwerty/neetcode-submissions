class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for i in strs:
            s += str(len(i)) + "#" + i

        return s

    def decode(self, s: str) -> List[str]:

        ans = []

        l = r = 0 
        n  = len(s)

        while r < n: 

            while s[r] != "#": 
                r += 1

            count = int(s[l:r])
            l = r + 1
            ans.append(s[l:l+count])

            l = l + count
            r = l 

        return ans 



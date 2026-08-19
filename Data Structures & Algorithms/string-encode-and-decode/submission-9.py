class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for i in range(len(strs)):

            s += str(len(strs[i])) + "#" + strs[i]

        return s

    def decode(self, s: str) -> List[str]:

        ans = []

        i = 0

        n = len(s)

        while i < n: 

            j = i 

            while j < n and s[j] != "#": 

                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j 

        return ans





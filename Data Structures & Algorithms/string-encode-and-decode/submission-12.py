class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""

        for i in strs: 
            encode += str(len(i)) + "#" + i

        return encode 

    def decode(self, s: str) -> List[str]:

        print(s)

        ans = []

        l = 0 

        n = len(s)

        while l < n:

            j = l 

            while j < n and s[j] != "#": 
                j += 1


            count = int(s[l:j]) # made  j -1 it will take loot time base i stack at here

            l = j + 1 
            j = l + count
          
            ans.append(s[l:j])

            l = j 
            print(l)

        return ans


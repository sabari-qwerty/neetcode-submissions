class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for i in strs: 

            if i == "": 
                s += "😅"
            else: 
                s += i
            s += "👨🏼‍🏭"
        

            

        return s

    def decode(self, s: str) -> List[str]:

        if s == "": return []

        ans = []

        for i in s.split("👨🏼‍🏭"):

            if i == "😅":
                ans.append("")
            else: 
                ans.append(i)

        return ans[:-1]
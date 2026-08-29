class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""

        for word in strs: 
            string += str(len(word)) + "#" + word

        return string 

    def decode(self, s: str) -> List[str]:
        print(s)

        l = 0 
        j = 0 

        n = len(s)

        ans = []

        while l < n: 

            j = l 

            while s[j] != "#" and j < n:
                j += 1
            count = int(s[l:j])
            l = j + 1
            print(s[j-1],s[l:l+count] )
            ans.append(s[l:l+count])
            
            l = l + count 

        return ans
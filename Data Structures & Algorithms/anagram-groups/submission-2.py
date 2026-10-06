class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hashMap = {}

        for char in strs: 

            freq = [0] * 26

            for cha in char: 

                diff = ord(cha) - ord('a') 

                freq[diff] += 1

            key = tuple(freq)

            if key in hashMap: 
                hashMap[key].append(char)
            else: 
                hashMap[key] = [char]


        return list(hashMap.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}


        for words in strs:

            freq = [0] * 26 

            for char in words: 

                freq[ord(char) - ord('a')] += 1

            key = tuple(freq) 

            if key  not in hashMap:
                hashMap[key] = [words]
            else: 
                hashMap[key].append(words)

        return list(hashMap.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:

            freq = [0] * 26

            for char in word:

                idx = ord(char) - ord('a')

                freq[idx] += 1

            key = tuple(freq)

            if key in hashMap:

                hashMap[key].append(word)
            else: 
                hashMap[key] = [word]

        return list(hashMap.values() )

 
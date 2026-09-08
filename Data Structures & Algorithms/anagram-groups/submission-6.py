class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for s in strs: 

            freq = [0] * 26

            for _ in s: 

                freq[ord('a') - ord(_)] += 1

            key = tuple(freq)

            if key not in hashMap:
                hashMap[key] = [s]
            else: 
                hashMap[key].append(s)

        return list(hashMap.values())

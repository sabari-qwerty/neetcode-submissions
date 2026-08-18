class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for word in strs: 

            freq = [0] * 26

            for ch in word:

                diff =  ord(ch)  - ord('a')

                freq[diff] += 1

            key = tuple(freq)

            value = hashMap.get(key, [])

            value.append(word)

            hashMap[key] = value

        return list(hashMap.values())
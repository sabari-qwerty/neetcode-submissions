class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}

        for word in strs: 

            freq = [0] * 26
            
            for ch in word:

                idx = ord(ch) - ord('a')

                freq[idx] += 1

            key = tuple(freq)

            array = hashMap.get(key, [])

            array.append(word)

            hashMap[key] = array


        return list(hashMap.values())
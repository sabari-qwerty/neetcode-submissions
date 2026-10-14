class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groupAngarams = {}

        for char in strs:

            key = [0] * 26

            for c in char:

                idx = ord(c) - ord('a')

                key[idx] += 1

            key = tuple(key)

            if key in groupAngarams: 
                groupAngarams[key].append(char)
            else: 
                groupAngarams[key] = [char]

        return list(groupAngarams.values())

            
            




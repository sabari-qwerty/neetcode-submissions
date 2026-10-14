class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groupAngarams = {}

        for char in strs:

            key = tuple(sorted(char))

            if key in groupAngarams:

                groupAngarams[key].append(char)
            else: 
                groupAngarams[key] = [char]

        return list(groupAngarams.values())





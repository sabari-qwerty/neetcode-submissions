class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = [ "".join(sorted(i)) for i in strs]

        hashMap = {}

        for i in range(len(strs)):

            if res[i] in hashMap: 
                hashMap[res[i]].append(strs[i])
            else: 
                hashMap[res[i]] = [strs[i]]

        return [i for i in  hashMap.values()]

        


        

        

        
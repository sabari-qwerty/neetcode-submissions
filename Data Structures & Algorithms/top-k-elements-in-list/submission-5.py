class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        max_count = 0 
        for key in nums: 
            numCount[key] = numCount.get(key, 0) + 1

            max_count = max(numCount[key], max_count)

        freqMap = {}

        for key, value in numCount.items(): 

            if value in freqMap: 
                freqMap[value].append(key)
            else: 
                freqMap[value] = [key]

        ans = []

        for i in range(max_count, -1, -1): 

            if i in freqMap:
                ans.extend(freqMap[i])
            else: continue

        return ans[:k]

        

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = {}

        for i in nums: 

            freq[i] = freq.get(i, 0) + 1

        buket = {}

        maxValue = 0

        for key, value in freq.items():

            maxValue = max(maxValue, value)
            
            if value in buket: 
                buket[value].append(key)
            else: 
                buket[value] = [key]

        res = []

        for i in range(maxValue):
            data = maxValue - i  

            if data in buket:
                res.extend(buket[data])

        return res[:k]
        
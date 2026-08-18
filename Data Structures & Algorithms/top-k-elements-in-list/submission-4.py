class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for i in nums: 
            hashMap[i] = hashMap.get(i, 0) +1

        bucket = {}


        for value, count in hashMap.items():

            if count in bucket: 
                bucket[count].append(value) 
            else: 
                bucket[count] = [value]


        res = []


        for i in range(len(nums), -1, -1): 

            if i in bucket: 
                res.extend(bucket[i])

        return res[:k]
        


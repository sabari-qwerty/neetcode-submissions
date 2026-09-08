class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count  = {}

        for i in nums: 

            if i in count: 
                count[i] += 1
            else: 
                count[i] = 1
        
        bucket = {}

        maxCount = 0

        for i in count:

            key =  count[i]

            if key in bucket: 
                bucket[key].append(i)
            else: 
                bucket[key] = [i]
            maxCount = max(maxCount, key)

        ans = []

        for i in range(maxCount, -1, -1): 

            if i in bucket: 
                ans.extend(bucket[i])

        return ans[:k]

            



        







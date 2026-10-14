class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}


        for i in nums: 
            count[i] = count.get(i, 0) + 1

        bucket = {}

        maxCount = 0

        for key, value in count.items():
            maxCount = max(maxCount, value)

            if value in bucket: 
                bucket[value].append(key)
            else: 
                bucket[value] = [key]

        ans = []

        for i in range(maxCount, -1, -1): 

            if i not in bucket: continue

            ans.extend(bucket[i])

            if len(ans) >= k: break

        return ans[:k]


        



 
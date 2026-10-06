class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = {} 

        maxFreq = 0 


        for i in nums: 

            if i in freq: 
                freq[i] += 1

            else: 
                freq[i] = 1
            
            maxFreq = max(maxFreq, freq[i])


        bucket = {}

        for key, value in freq.items():

            if value in bucket:
                bucket[value].append(key)
            else: 
                bucket[value] = [key]

        print(bucket)

        ans = []

        for i in range(maxFreq, -1, -1): 

            if i in bucket:

                for _ in bucket[i]:
                    ans.append(_)

                    if len(ans) == k:
                        return ans
        return ans









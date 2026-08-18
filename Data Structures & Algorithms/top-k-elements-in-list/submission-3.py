class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for i in nums: 

            hashMap[i] = hashMap.get(i, 0) + 1


        ans = [] 

        for _ in range(k):

            max_count = float('-inf')
            max_number = float('-inf')

            for number, count in hashMap.items():

                if count > max_count: 

                    max_count = count
                    max_number = number

            ans.append(max_number)
            del hashMap[max_number]

        return ans


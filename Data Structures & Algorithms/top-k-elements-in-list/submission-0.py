class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for i in nums: 

            hashMap[i] = hashMap.get(i, 0) +1

        sorted_array =  sorted(list(hashMap.items()), key=lambda x: x[1], reverse=True)

        return [i[0] for i in sorted_array][:k]

        
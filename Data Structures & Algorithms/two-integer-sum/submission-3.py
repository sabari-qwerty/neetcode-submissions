class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashMap = {}

        n = len(nums)


        for i in range(n): 

            diff = target - nums[i]

            if diff in hashMap: 
                return [hashMap[diff], i]

            hashMap[nums[i]] = i

        
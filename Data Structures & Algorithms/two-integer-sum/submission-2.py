class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i  in range(len(nums)): 

            diff = target - nums[i]

            if nums[i] in hashMap: 
                return [hashMap[nums[i]], i]

            hashMap[diff] = i

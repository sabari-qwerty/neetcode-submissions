class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for idx in range(len(nums)): 

            if nums[idx] in hashMap: 
                
                return [hashMap[nums[idx]], idx]

            diff = target - nums[idx]

            hashMap[diff] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)): 

            key = nums[i]

            diff = target - key 

            if diff in hashMap: 

                return [hashMap[diff], i]

            hashMap[key] = i

        return [-1, -1]
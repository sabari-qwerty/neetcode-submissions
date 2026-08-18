class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        n = len(nums)

        for i in range(n): 

            val = nums[i]

            cal = target - val

            if cal in hashMap: 
                return [hashMap[cal], i]

            hashMap[val] = i


        
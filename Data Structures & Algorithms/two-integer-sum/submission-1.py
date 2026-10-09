class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        n = len(nums)

        for i in range(n): 

            val = nums[i]

            diff = target - val

            if val in hashMap: 
                return [hashMap[val], i]

            hashMap[diff] = i

        return [-1, -1]
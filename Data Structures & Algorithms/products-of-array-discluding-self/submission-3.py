class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [1] * n
        prefix = 1

        zero_count = 0

        for i in range(n):

            ans[i] *= prefix
            prefix *= nums[i]

            if nums[i] == 0: 
                zero_count += 1

        if zero_count > 1: return [0] * len(nums)

        suffix = 1
        for i in range(n-1, -1, -1): 
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

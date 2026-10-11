class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        preSum = 1

        ans = [1] * n


        for i in range(1, n): 

            preSum *= nums[i-1]

            ans[i] = preSum


        sufSum = 1

        for i in range(n-2, -1, -1): 
            sufSum *= nums[i+1]

            ans[i] *= sufSum

        return ans




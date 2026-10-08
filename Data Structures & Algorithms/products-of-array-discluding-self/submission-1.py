class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        n = len(nums)

        ans = [1] * n 


        prefix = 1
        for i in range(1,len(nums)):

            prefix *=  nums[i-1]
            ans[i] *= prefix

        sufix = 1

        for i in range(len(nums)-2, -1, -1):

            sufix *= nums[i+1]
            ans[i] *= sufix







        return ans

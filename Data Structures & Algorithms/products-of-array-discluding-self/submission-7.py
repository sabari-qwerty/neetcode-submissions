class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [1] * n 

        preProd = 1

        for i in range(1, n): 
            preProd *= nums[i-1]
            ans[i] *= preProd

        
        suffixProd = 1

        for i in range(n-1, -1, -1): 

            ans[i] *= suffixProd

            suffixProd *= nums[i]

        return ans




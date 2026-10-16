class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        preProd = [1] * n 

        for i in range(1, n):

            preProd[i] = preProd[i-1] * nums[i-1]

        suffixProd =  [1] * n 

        for i in range(n-2, -1, -1): 

            suffixProd[i] = suffixProd[i+1] * nums[i+1]

        return [preProd[i] * suffixProd[i]  for i in range(n)]



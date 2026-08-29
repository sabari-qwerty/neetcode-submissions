class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = [1] * len(nums)

        n = len(nums)

        for i in range(1, n):

            prefix[i] *= prefix[i-1]  * nums[i - 1] 

        suffix = [1] * len(nums)

        for i in range(n-2, -1, -1):
            suffix[i] *= suffix[i+1] * nums[i+1] 

        return [ prefix[i] * suffix[i] for i in range(n)]

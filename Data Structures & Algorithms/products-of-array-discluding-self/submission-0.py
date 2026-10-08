class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [1] * n 

        for i in range(1,len(nums)):

            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * n 

        for i in range(len(nums)-2, -1, -1):

            suffix[i] = nums[i+1] * suffix[i+1]


        ans = []


        for i in range(n): 

            ans.append(prefix[i] * suffix[i])

        return ans

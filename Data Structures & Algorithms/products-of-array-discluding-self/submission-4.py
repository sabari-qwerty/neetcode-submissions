class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        preSum = [1] * n


        for i in range(1, n): 

            preSum[i] = preSum[i-1] * nums[i-1]  


        sufSumm = [1] * n 

        for i in range(n-2, -1, -1):
            sufSumm[i] = sufSumm[i+1] * nums[i+1]

        ans = []

        for i in range(n): 

            ans.append(sufSumm[i] * preSum[i])   

        


        return ans

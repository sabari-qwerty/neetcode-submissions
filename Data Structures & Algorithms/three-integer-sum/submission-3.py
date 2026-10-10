class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()

        ans = set()

        n = len(nums)


        for i in range(n):

            l = i + 1
            r = n -1

            if i > 0 and nums[i] == nums[i-1]: continue

            while l < r: 

                Sum = nums[i] + nums[l] + nums[r]

                if Sum == 0: 

                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1

                elif Sum > 0: 

                    r -= 1
                else: 
                    l += 1


    

        return [ list(i) for i in ans]
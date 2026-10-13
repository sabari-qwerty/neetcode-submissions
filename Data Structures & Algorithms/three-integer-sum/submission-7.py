class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()


        ans = set()

        n = len(nums)

        for i in range(n): 

            l = i + 1
            r = n - 1

            while l < r: 

                total = nums[i] + nums[l] + nums[r]

                if total == 0: 
                    key = (nums[i], nums[l], nums[r])
                    ans.add(key)
                    
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r: 
                        l += 1

                elif total > 0: 
                    r -= 1
                else: 
                    l += 1


        return [list(i) for i in  ans ]
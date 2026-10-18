class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = set()

        n = len(nums)

        for l in range(n): 
            m = l +1
            r = n -1

            while m < r: 

                Sum = nums[l] + nums[m] + nums[r]

                if Sum == 0: 
                    ans.add((nums[l], nums[m], nums[r]))
                    m += 1
                    r -= 1

                    
                    while nums[m-1] == nums[m] and m < r:
                        m += 1

                elif Sum > 0: 
                    r -=1
                else: 
                    m += 1
            
          



        return [list(tup) for tup in ans] 
 
        
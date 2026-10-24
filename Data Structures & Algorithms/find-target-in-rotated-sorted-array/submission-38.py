class Solution:


    def findPivat(self, nums):

        l = 0 
        r = len(nums) -1

        while l < r: 

            m = l + ((r - l) // 2)

            if nums[m] > nums[r]: 

                l = m + 1
            else: 
                r = m 

        return l 



    def searchValue(self, l, r, a, t):

        while l <= r:

            m = l +  ((r - l) // 2)  

            if a[m] == t: return m 
            elif a[m] > t: 
                r = m - 1
            else: 
                l = m + 1

        return -1




    def search(self, nums: List[int], target: int) -> int:

        pivat = self.findPivat(nums)

        if pivat > 0 and  nums[0] <= target:

            return self.searchValue(0, pivat, nums, target)

        else: 

            return self.searchValue(pivat, len(nums) -1, nums, target)

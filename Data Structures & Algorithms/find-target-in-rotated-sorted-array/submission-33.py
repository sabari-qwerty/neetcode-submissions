class Solution:

    def findPivat(self, nums):
        l = 0 
        r = len(nums) -1

        while l < r: 
            m = l + (r - l) // 2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m 

        return l

    def findTaget(self, l, r, nums, target):

        while l <= r: 
            m = l + (r - l) // 2

            if nums[m] == target: return m 
            elif nums[m] > target:
                r = m - 1
            else: 
                l = m + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:

        p = self.findPivat(nums)
        

        if p > 0 and nums[0] <= target:

            return self.findTaget(0, p, nums, target)

        else: 

            return self.findTaget(p, len(nums)-1, nums, target)
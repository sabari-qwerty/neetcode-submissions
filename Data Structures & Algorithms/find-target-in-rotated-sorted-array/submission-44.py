class Solution:

    def findPivot(self, nums):

        l = 0 
        r = len(nums) -1

        while l < r: 

            m = l + (r -l) // 2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m 

        return l  

    def findValue(self, nums, l, r, t):

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == t: return m

            if nums[m] > t: 
                r = m - 1
            else: 
                l = m + 1


        return -1

    def search(self, nums: List[int], target: int) -> int:

        pivot = self.findPivot(nums)

        if pivot > 0 and nums[0] <= target:

            return self.findValue(nums, 0, pivot, target)

        else: 

            return self.findValue(nums, pivot, len(nums) -1,  target)
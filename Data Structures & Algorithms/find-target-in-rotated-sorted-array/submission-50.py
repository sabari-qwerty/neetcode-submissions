class Solution:
    def findPivat(self, nums):

        r = len(nums) -1

        l = 0 

        while l < r:

            m = l + ((r - l) // 2)

            if nums[m] > nums[r]: 

                l = m +1
            else: 
                r = m 

        return l

    def findValue(self, l, r, arr, t): 

        while l <= r:
            m = l + ((r - l) // 2)

            if arr[m] == t: return m
            elif arr[m] > t:
                r = m -1
            else: 
                l = m +1 

        return -1
    def search(self, nums: List[int], target: int) -> int:

        p = self.findPivat(nums)

        if p > 0 and nums[0] <= target:

            return self.findValue(0, p, nums, target)

        else: 

            return self.findValue(p, len(nums)-1, nums, target)



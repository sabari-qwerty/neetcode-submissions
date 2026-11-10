class Solution:

    def findPivat(self, nums): 

        n = len(nums)

        l = 0 
        r = n - 1

        while l < r: 

            m = l +  ((r - l) // 2)

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m

        return l

    def findValue(self, l, r, nums, target):

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == target: return  m

            elif nums[m] > target: 
                r = m -1

            else: 
                l = m + 1

        return -1
    def search(self, nums: List[int], target: int) -> int:

        pivat = self.findPivat(nums)

        if pivat > 0 and nums[0] <= target:

            return self.findValue(0, pivat, nums, target)

        else: 
            return self.findValue( pivat, len(nums) -1,  nums, target)



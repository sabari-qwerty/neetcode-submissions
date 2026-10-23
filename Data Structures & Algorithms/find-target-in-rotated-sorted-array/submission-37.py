class Solution:

    def findMin(self, nums): 

        l = 0 
        r = len(nums) - 1

        while l < r: 

            m = (r - l) // 2  + l 

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m

        return l 

    def findTarget(self, l, r, nums, target): 

        while l <= r: 
            m = (r - l) // 2  + l 

            if nums[m] == target: return m

            elif nums[m] < target: 
                l = m +1
            else: 
                r = m -1

        return -1

    def search(self, nums: List[int], target: int) -> int:

        pivat = self.findMin(nums)

        if pivat > 0 and nums[0] <= target:

            return self.findTarget(0, pivat, nums, target)

        else: 
            return self.findTarget(pivat, len(nums) -1,  nums, target)

            
        
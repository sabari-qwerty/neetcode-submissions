class Solution:

    def pivatPoint(self, nums): 

        l = 0 
        r = len(nums) - 1

        while l < r: 

            m = l + ( r - l ) // 2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m 

        return l 

    def searchValue(self, l, r, nums, target): 

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == target: return m
            elif nums[m] < target: 
                l = m + 1
            else: 
                r = m - 1

        return -1


    def search(self, nums: List[int], target: int) -> int:

        pivat = self.pivatPoint(nums)

        if pivat > 0 and  nums[0] <= target: 
            return self.searchValue(0, pivat, nums, target)

        else: 
            print(pivat)
            return self.searchValue(pivat, len(nums)-1, nums, target)


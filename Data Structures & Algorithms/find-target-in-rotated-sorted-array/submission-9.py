class Solution:

    def findPivat(self, nums): 

        n = len(nums)

        r = n - 1

        l = 0 

        while l < r: 

            m = l +  (r - l) // 2 

            if nums[m] > nums[r]:
                l = m+ 1

            else: 
                r = m 

        return l

    def findTarget(self, nums, l, r, target): 

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == target: return m
            elif nums[m] < target: 
                l = m + 1
            else:
                r = m -1

        return -1





    def search(self, nums: List[int], target: int) -> int:
        

        pivat = self.findPivat(nums)


        if nums[pivat] <= target <= nums[-1]: 

            return self.findTarget(nums, pivat, len(nums)-1, target)
        else: 
            return self.findTarget(nums, 0, pivat-1, target)

            

        return 0
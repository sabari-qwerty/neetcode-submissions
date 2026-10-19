class Solution:

    def findPivot(self, nums): 

        l = 0 
        r = len(nums) - 1

        while l < r: 

            m = l + (r - l) // 2


            if nums[m] > nums[r]:

                l = m +1
            else: 
                r = m 

        return l  

    def findIndex(self, nums, l, r, target):

        while l <= r: 

            m = l + (r - l) // 2


            if nums[m] == target: return m
            elif nums[m] < target: 
                l = m+1
            else: 
                r = m-1
        return -1

    def search(self, nums: List[int], target: int) -> int:

        if not nums: return -1



        pivot = self.findPivot(nums)



        if nums[pivot] <=  target <= nums[-1]:
            return self.findIndex(nums, pivot, len(nums) -1, target ) 
        else: 
            return self.findIndex(nums, 0, pivot-1, target )



        
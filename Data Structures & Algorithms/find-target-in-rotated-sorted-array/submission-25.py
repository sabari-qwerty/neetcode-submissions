class Solution:

    def findPivot(self, nums): 
        l = 0 
        r = len(nums) - 1

        while l < r:

            m = l + (r - l) // 2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m 
        return l

    def findValue(self, l, r, nums, target): 

        while l <= r: 

            m = l + (r - l) // 2


            if nums[m] == target: return m
            elif nums[m] < target: 
                l = m + 1
            else: 
                r = m - 1

        return -1




    def search(self, nums: List[int], target: int) -> int:
        pivot =  self.findPivot(nums)

        print(pivot)



        if pivot > 0 and target >= nums[0] :

            return self.findValue(0, pivot, nums, target)

        else: 

            return self.findValue(pivot, len(nums)-1, nums, target)






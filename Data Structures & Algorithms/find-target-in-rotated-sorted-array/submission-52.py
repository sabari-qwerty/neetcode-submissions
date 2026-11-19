class Solution:

    def findMid(self, arr): 

        r = len(arr) - 1

        l = 0 

        while l < r: 

            m = l + ((r - l) // 2)

            if arr[m] > arr[r]: 
                l = m + 1
            else: 
                r = m 

        return l 

    def findValue(self, l, r, arr, target): 

        while l <= r: 

            m = l + ((r - l) // 2)

            if arr[m] == target: return m

            if arr[m] < target: 

                l = m + 1
            else: 
                r = m - 1

        return -1


    def search(self, nums: List[int], target: int) -> int:

        pivat = self.findMid(nums)

        if pivat > 0 and nums[0] <=  target:

            return self.findValue(0, pivat, nums, target)

        else: 
            return self.findValue(pivat, len(nums)-1, nums, target)


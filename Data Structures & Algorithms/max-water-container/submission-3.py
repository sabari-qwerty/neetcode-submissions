class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        l = 0 
        r = n -1 

        maxHeight = 0

        while l < r: 

            length = r - l 

            minWhaterContinLevel = min(heights[r], heights[l])

            maxHeight = max(maxHeight,minWhaterContinLevel * length)

            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1 

        return maxHeight


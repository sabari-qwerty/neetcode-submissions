class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxValue = 0 

        l = 0 
        r = len(heights) -1

        while l < r:

            diff = r - l 

            min_wall = min(heights[r], heights[l])

            maxValue = max(maxValue, diff * min_wall)
 

            if heights[l] < heights[r] or heights[l] == heights[r]: 
                l += 1
            else: 
                r -= 1

        return maxValue
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) -1

        max_area = 0 


        while l < r:

            lenght = r - l 

            area = min(heights[l], heights[r]) * lenght

            max_area = max(area, max_area)

            if heights[l] < heights[r]: 
                l += 1

            else: 
                r -= 1

        return max_area



        
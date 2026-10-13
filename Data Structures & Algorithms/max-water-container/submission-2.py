class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights) 

        l = 0
        r = n - 1

        maxLength = 0 

        while l < r:

            minLength = min(heights[l], heights[r])

            maxLength = max(maxLength, minLength * (r - l))

            if heights[l] < heights[r]: 
                l += 1
            else: 

                r -= 1

        return maxLength

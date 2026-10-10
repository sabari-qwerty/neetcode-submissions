class Solution:
    def maxArea(self, h: List[int]) -> int:

        n = len(h)

        max_area = 0 

        l = 0 
        r = n -1

        while l < r: 

            area = min(h[l], h[r]) * (r - l)
            max_area = max(area, max_area) 

            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1

        return max_area  



            
        
class Solution:
    def maxArea(self, h: List[int]) -> int:

        n = len(h)

        max_area = 0 

        l = 0 
        r = n -1

        while l < r: 

            area = min(h[l], h[r]) * (r - l)
            max_area = max(area, max_area) 

            min_hight = min(h[l], h[r])


            while l < r and h[l] <= min_hight: 
                l += 1

            while l < r and h[r] <= min_hight:
                r -= 1


        return max_area  



            
        
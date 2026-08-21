class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        porfit = 0 

        n = len(prices)

        if len(prices) == 1: return 0

        l = 0 
        r = 1


        while r < n: 

            if prices[l] > prices[r]:
                l = r
                r += 1
            else: 
                porfit = max(porfit,  prices[r] - prices[l])

                r += 1

        return porfit 




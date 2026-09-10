class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        porfit = 0 

        minPrice = prices[0]

        for i in range(1, len(prices)):

            minPrice = min(prices[i], minPrice)
            porfit = max(porfit, prices[i] - minPrice)

        return porfit






class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_porfit = 0 

        price = prices[0]

        n = len(prices)

        for i in range(1, n): 

            if price > prices[i]:
                price =  prices[i]
                continue

            max_porfit = max(max_porfit, prices[i] - price )

        return max_porfit

            

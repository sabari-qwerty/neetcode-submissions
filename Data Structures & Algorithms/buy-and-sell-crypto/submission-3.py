class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]

        n = len(prices)

        max_porfit = 0


        for i in range(1, n): 

            if min_price > prices[i]: 
                min_price = prices[i]
                continue

            max_porfit = max(max_porfit,prices[i] - min_price  )
            


        return max_porfit
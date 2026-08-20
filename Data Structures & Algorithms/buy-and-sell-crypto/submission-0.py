class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        profit = 0

        for i in range(n): 

            for j in range(i+1, n): 

                if prices[j] - prices[i]: 

                    profit = max(prices[j] - prices[i],profit)

        return profit

                
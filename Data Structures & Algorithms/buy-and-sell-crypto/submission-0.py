class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0 

        n = len(prices)

        for l in range(n): 
            for r in range(l+1, n):


                max_price = max(prices[r] - prices[l], max_price) 

        return  max_price 
        
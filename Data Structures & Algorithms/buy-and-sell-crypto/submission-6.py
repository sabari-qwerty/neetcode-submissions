class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxPorfit = 0 

        bestPriceToBy = prices[0]

        n = len(prices)

        for i in range(1, n):

            if  bestPriceToBy > prices[i]: 

                bestPriceToBy = prices[i]

            else:

                maxPorfit = max(maxPorfit, prices[i] - bestPriceToBy )





        return maxPorfit 
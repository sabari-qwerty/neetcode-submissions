class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_porfit = 0 

        n = len(prices)

        min_pice = prices[0]

        for i in range(1, n):

            if  min_pice > prices[i]: 
                min_pice = prices[i]
                continue

            porfit = prices[i] - min_pice

            max_porfit = max(porfit, max_porfit)

        return max_porfit
            

    


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        l = 0 
        r = 1

        maxPrise = 0 
        while r < n:

            if  prices[l] < prices[r]:
                maxPrise = max(prices[r] - prices[l], maxPrise)
                r += 1
            else: 
                l = r
                r = r +1

        return maxPrise
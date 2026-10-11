class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        max_price = 0


        if n == 1:return max_price

        idx = 1

        min_price = prices[0]


        while idx < n: 

            if min_price > prices[idx]: 

                min_price = prices[idx]
                continue 

            max_price = max(max_price, prices[idx] - min_price)


            idx += 1

        return max_price

                


    
 


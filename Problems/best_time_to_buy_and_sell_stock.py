class Solution(object):

    def maxProfit(self, prices):

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            
            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit
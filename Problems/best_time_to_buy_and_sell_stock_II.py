# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
             max_profit += prices[i] - prices[i-1]

        return max_profit
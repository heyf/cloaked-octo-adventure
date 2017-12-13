# 122. Best Time to Buy and Sell Stock II - LeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        if len(prices) == 0:
            return total_profit
        have_stock_price = -1
        i = 1
        while i < len(prices):
            if have_stock_price > -1:
                if prices[i] < prices[i-1]:
                    total_profit += prices[i-1] - have_stock_price
                    have_stock_price = -1
            else: # Don't have stock, curr means current min
                if prices[i] > prices[i-1]: # have profit, buy
                    have_stock_price = prices[i-1]
            i += 1
        if have_stock_price > -1:
            total_profit += prices[-1] - have_stock_price
        return total_profit
        
s = Solution()
print(s.maxProfit([1,5,10,10,5,1]))
print(s.maxProfit([2,1,2,0,1]))
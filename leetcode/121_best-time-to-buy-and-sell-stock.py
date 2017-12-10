# 121. Best Time to Buy and Sell Stock - LeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_prices = prices[0]
        res = 0
        for i in prices:
            min_prices = min( min_prices, i )
            res = max( res, i - min_prices )
        return res
        
        
pairs = [
    ([7, 1, 5, 3, 6, 4],5),
    ([7, 6, 4, 3, 1],0),
    ([1,5,0,3],4),
]

s = Solution()

for i in pairs:
    r = s.maxProfit(i[0])
    print(r,r==i[1])
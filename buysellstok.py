class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        lowest = prices[0]
        highest = 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > highest:
                highest = price - lowest
        return highest
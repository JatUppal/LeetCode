class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                profit = prices[i] - lowest
                maxProfit = max(profit, maxProfit)
        return maxProfit
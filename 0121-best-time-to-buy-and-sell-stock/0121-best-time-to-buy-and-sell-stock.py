class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        total = 0
        for p in prices:
            if p < lowest:
                lowest = p
            else:
                profit = p - lowest
                total = max(total, profit)
        return total
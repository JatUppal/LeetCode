class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("infinity")] * (amount + 1)
        dp[0] = 0
        c = 0
        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], 1 + dp[x - c])
        if dp[amount] != float("infinity"):
            return dp[amount]
        else:
            return -1
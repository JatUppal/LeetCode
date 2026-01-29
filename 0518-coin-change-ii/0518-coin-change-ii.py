class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] = number of ways to make amount 'a'
        dp = [0] * (amount + 1)
        # There is exactly 1 way to make 0: choose no coins
        dp[0] = 1
        # Loop coins first to count combinations (order doesn't matter)
        for coin in coins:
            # For each amount >= coin, add ways that include this coin
            for a in range(coin, amount + 1):
                # If we use 'coin', then we need to make (a - coin) in any valid way
                dp[a] += dp[a - coin]
        # Answer: ways to make the target amount
        return dp[amount]
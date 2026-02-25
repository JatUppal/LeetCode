class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [float("infinity")] * (amount + 1)
        a[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    a[i] = min(a[i], a[i - coin] + 1)
        if a[amount] != float("infinity"):
            return a[amount]
        else:
            return -1


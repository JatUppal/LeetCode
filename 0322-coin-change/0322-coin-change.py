class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [float("infinity")] * (amount + 1)
        a[0] = 0
        for i in range(len(a)):
            for c in coins:
                if c > i:
                    continue
                remain = i - c
                a[i] = min(a[i], a[remain] + 1)
        return a[amount] if a[amount] != float("infinity") else -1
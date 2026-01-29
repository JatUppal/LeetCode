class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Memoization map: number -> number of steps to reach 1
        # Base case: 1 takes 0 steps
        steps = {1: 0}
        # Compute power values for all numbers in range [lo, hi]
        for x in range(lo, hi + 1):
            cur = x
            path = []  # Track numbers until we hit a known value
            # Follow Collatz rules until we reach a number already computed
            while cur not in steps:
                path.append(cur)
                if cur % 2 == 0:
                    cur = cur // 2
                else:
                    cur = 3 * cur + 1
            # Start with the known power value we reached
            power = steps[cur]
            # Walk back through the path and assign power values
            # in reverse so each number builds on the previous
            for v in reversed(path):
                power += 1
                steps[v] = power
        # Create list of numbers in range
        arr = list(range(lo, hi + 1))
        # Sort by (power value, number) as required by the problem
        arr.sort(key=lambda x: (steps[x], x))
        # Return the k-th element (1-indexed)
        return arr[k - 1]
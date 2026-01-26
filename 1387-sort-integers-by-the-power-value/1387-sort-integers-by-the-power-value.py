class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        steps = {}
        for x in range(lo, hi + 1):
            total = 0
            original = x
            cur = x
            while cur != 1:
                if cur in steps:
                    total += steps[cur]
                    break
                if cur % 2 == 0:
                    cur = cur // 2
                else:
                    cur = 3 * cur + 1
                total += 1
            steps[original] = total
        arr = sorted(steps, key=lambda x: (steps[x], x))
        return arr[k-1]
        

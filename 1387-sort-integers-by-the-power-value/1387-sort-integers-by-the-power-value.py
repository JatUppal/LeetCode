class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        steps = {1:0}
        for x in range(lo, hi + 1):
            cur = x
            path = []
            while cur not in steps:
                path.append(cur)
                if cur % 2 == 0:
                    cur = cur // 2
                else:
                    cur = 3 * cur + 1
            power = steps[cur]
            for v in reversed(path):
                power += 1
                steps[v] = power

        arr = list(range(lo, hi + 1))
        arr.sort(key=lambda x: (steps[x], x))
        return arr[k-1]
        

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1
        if target == start:
            return 0
        def neighbors(code):
            res = []
            for i in range(4):
                d = int(code[i])
                for nd in ((d + 1) % 10, (d - 1) % 10):
                    res.append(code[:i] + str(nd) + code[i+1:])
            return res
        q = deque([(start, 0)])
        visited = {start}
        while q:
            code, steps = q.popleft()
            for nxt in neighbors(code):
                if nxt in dead or nxt in visited:
                    continue
                if nxt == target:
                    return steps + 1
                visited.add(nxt)
                q.append((nxt, steps + 1))
        return -1
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mask = [-cnt for cnt in count.values()]
        heapq.heapify(mask)
        q = deque()
        time = 0
        while mask or q:
            time += 1
            if mask:
                cnt = heapq.heappop(mask) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(mask, q.popleft()[0])
        return time

        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            rock1 = heapq.heappop(stones)
            rock2 = heapq.heappop(stones)
            if rock2 > rock1:
                heapq.heappush(stones, rock1 - rock2)
        stones.append(0)
        return abs(stones[0])
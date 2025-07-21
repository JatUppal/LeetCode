class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            d = (math.sqrt((y - 0) ** 2 + (x - 0) ** 2))
            dist.append((d, (x,y)))
        dist.sort()
        return [p for _, p in dist[:k]]
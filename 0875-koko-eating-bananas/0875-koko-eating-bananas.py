class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def check(speed : int):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours
        while l < r:
            mid = (l + r) // 2
            if check(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return r
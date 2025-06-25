class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []

        self.times[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.times.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = ((l + r) // 2)
            if values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0]
                if values[mid][1] == timestamp:
                    break
                l = mid + 1
        return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = []
        res.append(intervals[0])
        current_end = intervals[0][1]
        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if current_end >= next_start:
                res[-1][1] = max(current_end, next_end)
                current_end = res[-1][1]
            else:
                res.append([next_start, next_end])
                current_end = next_end
        return res
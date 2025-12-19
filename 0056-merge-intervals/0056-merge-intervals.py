class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curr_start, curr_end = intervals[0]
        for s,e in intervals[1:]:
            if s <= curr_end:
                curr_end = max(curr_end, e)
            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = s, e
        res.append([curr_start, curr_end])
        return res
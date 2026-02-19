class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        s = 0
        e = 0
        maxRooms = 0
        rooms = 0
        while s < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            maxRooms = max(maxRooms, rooms)
        return maxRooms
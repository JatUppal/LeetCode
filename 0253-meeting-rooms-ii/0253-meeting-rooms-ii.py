class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        start.sort()
        end.sort()
        s = 0
        e = 0
        maxRooms = 0
        rooms = 0
        while s < len(start):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            maxRooms = max(rooms, maxRooms)
        return maxRooms
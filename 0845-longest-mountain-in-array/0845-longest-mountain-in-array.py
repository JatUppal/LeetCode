class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        res = 0
        up = 0
        down = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if down > 0:
                    up = 0
                    down = 0
                up += 1
            elif arr[i] < arr[i - 1] and up > 0:
                down += 1
            elif arr[i] == arr[i - 1]:
                up, down = 0, 0
            if up > 0 and down > 0:
                res = max(res, 1 + up + down)
        return res
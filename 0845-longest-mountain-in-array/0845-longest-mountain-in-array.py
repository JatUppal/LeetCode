class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up = 0
        down = 0
        res = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if down > 0:
                    down = 0
                    up = 0
                up += 1
            elif arr[i] > arr[i + 1]:
                down += 1
            else:
                up = 0
                down = 0
            if i >= 1 and up > 0 and down > 0:
                res = max(res, up + down + 1)
        return res
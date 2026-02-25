class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up = 0
        down = 0
        longest = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if down > 0:
                    up = 0
                    down = 0
                up += 1
            elif arr[i] > arr[i + 1]:
                if up > 0:
                    down += 1
            else:
                up = 0
                down = 0
            if up > 0 and down > 0:
                longest = max(longest, up + down + 1)
        return longest

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]
        drop = float("-inf")
        res = arr[0]
        for i in arr[1:]:
            drop = max(drop + i, keep)
            keep = max(keep + i, i)
            res = max(res, keep, drop)
        return res
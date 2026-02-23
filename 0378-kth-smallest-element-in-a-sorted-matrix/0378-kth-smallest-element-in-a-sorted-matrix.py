class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = 0
        n = len(matrix)
        l = matrix[0][0]
        h = matrix[n - 1][n-1]
        def count_le(x):
            c = 0
            r = n - 1
            cnt = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= x:
                    cnt += r + 1
                    c += 1
                else:
                    r -= 1
            return cnt
        while l < h:
            mid = (l + h) // 2
            if count_le(mid) < k:
                l = mid + 1
            else:
                h = mid
        return l
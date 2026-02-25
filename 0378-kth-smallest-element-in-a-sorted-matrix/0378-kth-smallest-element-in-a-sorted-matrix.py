class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        h = matrix[n-1][n-1]
        def count_steps(num : int):
            r = n - 1
            c = 0
            steps = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= num:
                    steps += r + 1
                    c += 1
                else:
                    r -= 1
            return steps
        while l < h:
            mid = (l + h) // 2
            if count_steps(mid) < k:
                l = mid + 1
            else:
                h = mid
        return l
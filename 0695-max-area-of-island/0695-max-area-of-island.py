class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i, j))
            up = dfs(i + 1, j)
            down = dfs(i - 1, j)
            right = dfs(i, j + 1)
            left = dfs(i, j - 1)
            return 1 + up + down + right + left

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)
        return maxArea
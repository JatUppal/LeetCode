class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Depth-first search to mark all connected land as visited
        def dfs(row, col):
            # Stop if out of bounds or already water
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0":
                return
            # Mark current land cell as visited
            grid[row][col] = "0"
            # Explore all four directions
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)
        # Counts number of islands
        counter = 0
        # Traverse every cell in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If land is found, it's a new island
                if grid[row][col] == "1":
                    counter += 1
                    # Mark the entire island as visited
                    dfs(row, col)
        # Return total number of islands
        return counter
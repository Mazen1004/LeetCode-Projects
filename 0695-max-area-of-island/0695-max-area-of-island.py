class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            # Mark the cell as visited by setting it to 0
            grid[row][col] = 0
            size = 1  # Start with size 1 (current cell)
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col):
                    size += dfs(next_row, next_col)
            
            return size
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maxSize = 0
        m = len(grid)
        n = len(grid[0])
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    # Perform DFS and get the size of the current island
                    size = dfs(row, col)
                    # Update the maximum size of the island found so far
                    maxSize = max(maxSize, size)
        
        return maxSize
        
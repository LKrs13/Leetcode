class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res
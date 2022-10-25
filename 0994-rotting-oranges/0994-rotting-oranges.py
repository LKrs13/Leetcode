from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten, fresh = deque([]), set()
        ct = -1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                
                if grid[r][c] == 2:
                    rotten.append((r, c))
        
        while rotten:
            ct += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                
                for dr, dc in (1,0), (-1,0), (0,1), (0,-1):
                    nr, nc = r + dr, c + dc
                    
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh.remove((nr, nc))
                        rotten.append((nr, nc))
        if fresh:
            return -1
        
        return ct if ct != -1 else 0
        
        
        
        
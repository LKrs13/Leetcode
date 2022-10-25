from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        gates = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append((r, c))
        
        while gates:
            for _ in range(len(gates)):
                r, c = gates.popleft()
                
                for dr, dc in (0,1), (0,-1), (1,0), (-1,0):
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < rows and 0 <= nc < cols) and rooms[nr][nc] > rooms[r][c] + 1:
                        gates.append((nr, nc))
                        rooms[nr][nc] = rooms[r][c] + 1
                
        
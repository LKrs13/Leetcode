class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        Start from the Os at the borders and make search on the
        neighboring Os to mark those as non flippable
        Flip the flippable Os
        """
        rows, cols = len(board), len(board[0])
        nf = set()
        
        def dfs(r, c, s):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            
            if board[r][c] == "X":
                return
            
            if (r, c) in s:
                return
            
            s.add((r, c))
            
            for nr, nc in (0,1), (0,-1), (1,0), (-1,0):
                dfs(r + nr, c + nc, s)
            
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    dfs(r, c, nf)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in nf:
                    board[r][c] = "X"
        
        return board
                
        
        
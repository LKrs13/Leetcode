class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            row = [x for x in board[r] if x.isdigit()]
            if len(set(row)) != len(row):
                return False
        
        transposed = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(board[c][r])
            transposed.append(row)
        
        for r in range(rows):
            row = [x for x in transposed[r] if x.isdigit()]
            if len(set(row)) != len(row):
                return False
        
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                box = board[r][c:c+3] + board[r+1][c:c+3] + board[r+2][c:c+3]
                box = [x for x in box if x.isdigit()]
                if len(set(box)) != len(box):
                    return False
        
        return True 
                
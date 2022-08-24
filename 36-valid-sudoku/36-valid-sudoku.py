class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def repetitionChecker(row):
            ct = Counter(row)
            for i, j in ct.items():
                if i != "." and j > 1:
                    return False
            return True
        
        for row in board:
            if not repetitionChecker(row):
                return False
        
        t = list(zip(*board))
        for col in t:
            if not repetitionChecker(col):
                return False
        
        for r in range(0, 9, 3):
            for i in range(0, 9, 3):
                x = board[r][i:i+3] + board[r+1][i:i+3] + board[r+2][i:i+3]
                if not repetitionChecker(x):
                    return False
        
        return True 
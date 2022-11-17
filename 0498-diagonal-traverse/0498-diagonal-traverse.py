from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonalDict = defaultdict(list)
		
        # key - diagonal elements have the same r + c value.
        for r in range(rows):
            for c in range(cols):
                diagonalDict[r+c].append(mat[r][c])
        
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
                
        return ans
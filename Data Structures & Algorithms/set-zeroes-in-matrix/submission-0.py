class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROW,COL = len(matrix),len(matrix[0])
        
        row,col=set(),set()

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        
        for r in row:
            for j in range(COL):
                matrix[r][j]=0
        
        for c in col:
            for i in range(ROW):
                matrix[i][c]=0
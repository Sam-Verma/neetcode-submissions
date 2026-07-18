class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        for r in range(n):
            for c in range(r,n):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
        
        
        for row in matrix:
            i,j=0,len(row)-1
            while i<j:
                row[i],row[j]=row[j],row[i]
                i+=1
                j-=1
        
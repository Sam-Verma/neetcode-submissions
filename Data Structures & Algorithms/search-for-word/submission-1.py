class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROW,COL = len(board),len(board[0])
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        def backtrack(r,c,i):
            
            if i==len(word):
                return True

            if r<0 or c<0 or r>=ROW or c>=COL or board[r][c]!=word[i] or visited[r][c]:
                return False
            
            visited[r][c]=True
            res = backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)
            visited[r][c]=False
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack(r,c,0):
                    return True

        return False
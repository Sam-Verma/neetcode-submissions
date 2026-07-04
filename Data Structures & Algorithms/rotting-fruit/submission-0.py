class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROW,COL = len(grid),len(grid[0])
        count=0
        
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        rotton=deque()
        fresh=0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    rotton.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        while rotton and fresh>0:
            
            for _ in range(len(rotton)):
                r,c = rotton.popleft()

                for dr,dc in dir:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        rotton.append((nr,nc))
                    
            count+=1

        return count if fresh==0 else -1        
            
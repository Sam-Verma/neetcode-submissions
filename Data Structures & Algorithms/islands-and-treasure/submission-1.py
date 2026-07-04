class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROW,COL = len(grid),len(grid[0])
        inf = 2147483647

        chest = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    chest.append((r,c))
        
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        while chest:
            box=len(chest)
            for _ in range(box):
                r,c = chest.popleft()
                visited[r][c]=True
                for dr,dc in dir:
                    nr,nc=r+dr,c+dc
                    if (0<=nr<ROW and 0<=nc<COL and visited[nr][nc]==False and grid[nr][nc]==inf):
                        grid[nr][nc]=grid[r][c]+1
                        chest.append((nr,nc))
                        visited[nr][nc]=True
    

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        dirc=[(0,-1),(0,1),(1,0),(-1,0)]
        l=len(grid)
        w=len(grid[0])
        for i in range(l):
            for j in range(w):
                if grid[i][j]==1:
                    res+=4
                    for dx,dy in dirc:
                        ni=i+dx
                        nj=j+dy
                        if ni<l and ni>=0 and nj<w and nj>=0 and grid[ni][nj]==1:
                            res-=1
        return res
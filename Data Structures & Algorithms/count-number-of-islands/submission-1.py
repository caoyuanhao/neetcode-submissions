class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        l=len(grid)
        w=len(grid[0])
        def dfs(row,col):
            if row<0 or col<0 or row>=l or col>=w:
                return
            
            if grid[row][col]=="0":
                return
            grid[row][col]="0"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for r in range(l):
            for c in range(w):
                if grid[r][c]=="1":
                    res+=1
                dfs(r,c)
        return res
                

            
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dist=[[float("inf")]*len(grid[0]) for _ in range(len(grid))]
        dist[0][0]=grid[0][0]
        heap=[(grid[0][0],0,0)]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            d,r,c=heapq.heappop(heap)
            if d>dist[r][c]:
                continue

            if r == len(grid)-1 and c == len(grid[0])-1:
                return d
            
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                newDist=max(d,grid[nr][nc])

                if newDist<dist[nr][nc]:
                    dist[nr][nc]=newDist
                    heapq.heappush(heap,(newDist,nr,nc))
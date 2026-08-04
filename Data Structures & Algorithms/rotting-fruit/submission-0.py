class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        m=0
        fresh=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        while queue:
            s=len(queue)
            infected=False
            for _ in range(s):
                r,c=queue.popleft()
                if r+1<len(grid) and grid[r+1][c]==1:
                    grid[r+1][c]=2
                    infected=True
                    fresh-=1
                    queue.append((r+1,c))
                if r-1>=0 and grid[r-1][c]==1:
                    grid[r-1][c]=2
                    infected=True
                    fresh-=1
                    queue.append((r-1,c))
                if c+1<len(grid[0]) and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    infected=True
                    fresh-=1
                    queue.append((r,c+1))
                if c-1>=0 and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    infected=True
                    fresh-=1
                    queue.append((r,c-1))
            if infected:
                m+=1
            
        
        if fresh!=0:
            return -1
        else:
            return m


        
        
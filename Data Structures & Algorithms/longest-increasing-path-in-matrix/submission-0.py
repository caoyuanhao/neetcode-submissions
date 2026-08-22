class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c):
            if memo[r][c]!=0:
                return memo[r][c]
            res=1

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr>=len(matrix) or nc>=len(matrix[0]) or nc<0 or nr<0:
                    continue
                if matrix[nr][nc]<=matrix[r][c]:
                    continue
                res=max(res,1+dfs(nr,nc))
            memo[r][c]=res
            return res
        res=0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res=max(res,dfs(r,c))
        return res
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dq=[[0]*n for _ in range(m)]
        for i in range(m):
            dq[i][0]=1
        for j in range(n):
            dq[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dq[i][j]=dq[i-1][j]+dq[i][j-1]
        return dq[m-1][n-1]
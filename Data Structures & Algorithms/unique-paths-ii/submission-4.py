class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        l,w=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[float("inf")]*w for _ in range(l)]
        for i in range(l):
            for j in range(w):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
        dp[0][0]=1
        for i in range(1,l):
            if dp[i][0]==0:
                continue
            dp[i][0]=dp[i-1][0]
        for j in range(1,w):
            if dp[0][j]==0:
                continue
            dp[0][j]=dp[0][j-1]
        
        for i in range(1,l):
            for j in range(1,w):
                if dp[i][j]==0:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
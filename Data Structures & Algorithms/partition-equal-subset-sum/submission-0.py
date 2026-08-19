class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        half=int(total/2)
        dp=[False]*(half+1)
        dp[0]=True
        for i in nums:
            for j in range(half,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[half]

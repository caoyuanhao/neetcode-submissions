class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        dp=[[0]*len(nums) for _ in range(len(nums))]
        for length in range(2,len(nums)):
            for l in range(len(nums)-length):
                r=l+length
                for k in range(l+1,r):
                    dp[l][r]=max(dp[l][r],dp[l][k]+dp[k][r]+nums[l]*nums[k]*nums[r])
        return dp[0][len(nums)-1]
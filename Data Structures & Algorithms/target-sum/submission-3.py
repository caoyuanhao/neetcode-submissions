class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)

        p=(total+target)//2
        if abs(target)>total:
            return 0
        if (total+target)%2!=0:
            return 0
        dp=[0]*int(p+1)
        dp[0]=1
        for num in nums:
            for i in range(int(p),num-1,-1):
                dp[i]+=dp[i-num]
        return dp[p]




class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        if len(s)>0:
            dp[0]=1
            if s[0]=="0":
                dp[1]=0
            else:
                dp[1]=1
        else:
            return 0
        for i in range(2,len(s)+1):
            if s[i-1]!="0":
                dp[i]+=dp[i-1]
            if 9<int(s[i-2:i])<27:
                dp[i]+=dp[i-2]
        return dp[-1]

            
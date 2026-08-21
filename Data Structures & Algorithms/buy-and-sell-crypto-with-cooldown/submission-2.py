class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding=[0]*(len(prices))
        sold=[0]*len(prices)
        cooldown=[0]*len(prices)
        holding[0]=-prices[0]
        sold[0]=float("-inf")
        for i in range(1,len(prices)):
            holding[i]=max(holding[i-1],cooldown[i-1]-prices[i])
            sold[i]=holding[i-1]+prices[i]
            cooldown[i]=max(cooldown[i-1],sold[i-1])
        return max(sold[-1],cooldown[-1])


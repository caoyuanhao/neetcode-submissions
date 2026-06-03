class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,0
        res=0
        while right<len(prices)-1:
            right+=1
            if prices[right]>prices[left]:
                res=max(res,prices[right]-prices[left])
            else:
                left=right
                res=max(res,prices[right]-prices[left])
        return res
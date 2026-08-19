class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            newmax=max(nums[i],curmax*nums[i],curmin*nums[i])
            newmin=min(nums[i],curmax*nums[i],curmin*nums[i])
            curmax=newmax
            curmin=newmin
            res=max(curmax,res)
        return res
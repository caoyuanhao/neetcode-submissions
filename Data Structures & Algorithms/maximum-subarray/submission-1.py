class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        res=nums[0]
        if len(nums)==1:
            return nums[0]
        for i in nums:
            
            if cur_sum<0:
                cur_sum=0
            cur_sum+=i
            res=max(cur_sum,res)
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[1]*l

        left=1
        for i in range(l):
            res[i]=left
            left*=nums[i]
        
        right=1
        for i in range(l-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        
        return res


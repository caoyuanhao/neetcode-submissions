class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for left in range(len(nums)-k+1):
            temp=nums[left:left+k]
            temp=sorted(temp)
            res.append(temp[-1])
        return res
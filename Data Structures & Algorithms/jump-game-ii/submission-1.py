class Solution:
    def jump(self, nums: List[int]) -> int:
        max_sum=0
        res=0
        cur_end=0
        for i in range(len(nums)-1):
            max_sum=max(max_sum,nums[i]+i)
            if i==cur_end:
                cur_end=max_sum
                res+=1
                if max_sum>=len(nums)-1:
                    return res
        return 0
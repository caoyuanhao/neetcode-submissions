class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set=set(nums)
        if nums==[]:
            return 0
        res=1
        for x in nums_set:
            if x-1 not in nums_set:
                l=1
                while x+l in nums_set:
                    l+=1
                    res=max(res,l)
        return res
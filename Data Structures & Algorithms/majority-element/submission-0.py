class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=nums[0]
        flags=0
        for num in nums:
            if n==num:
                flags+=1
            else:
                flags-=1
            if flags<0:
                n=num
                flags=1
        return n
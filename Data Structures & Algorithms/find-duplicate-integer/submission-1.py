class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=0
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        res=[x for x,c in d.items() if c>1]
        return res[0]
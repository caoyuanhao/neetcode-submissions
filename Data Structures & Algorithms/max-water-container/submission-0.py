class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        res=0
        while left<right:
            l=heights[left]
            r=heights[right]
            c=min(l,r)*(right-left)
            res=max(res,c)
            if l<r:
                left+=1
            else:
                right-=1
        return res
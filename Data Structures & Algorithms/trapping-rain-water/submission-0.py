class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        res=0
        l=height[left]
        r=height[right]
        while left<right:
            if l<=r:
                left+=1
                l=max(l,height[left])
                res+=l-height[left]
            if r<l:
                right-=1
                r=max(r,height[right])
                res+=r-height[right]
        return res
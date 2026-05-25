class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        for x in range(len(heights)):
            if x==0:
                right=x+1
                while right<=len(heights)-1 and heights[x]<=heights[right]:
                    right+=1
                res=max(res,right*heights[x])
            elif x==len(heights)-1:
                left=x-1
                while left>=0 and heights[x]<=heights[left]:
                    left-=1
                res=max(res,(x-left)*heights[x])
            else:
                right=x+1
                left=x-1
                while right<=len(heights)-1 and heights[x]<=heights[right]:
                    right+=1                
                while left>=0 and heights[x]<=heights[left]:
                    left-=1
                res=max(res,(right-left-1)*heights[x])
        return res
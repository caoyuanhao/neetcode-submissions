class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        heights=heights+[0]
        for i,x in enumerate(heights):
            while stack and x<heights[stack[-1]]:
                j=stack.pop()
                if stack:
                    left=stack[-1]
                else:
                    left=-1
                res=max(res,(i-left-1)*heights[j])
            stack.append(i)
        return res
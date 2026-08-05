class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        qp=deque()
        qa=deque()
        visitedp=[[False]*len(heights[0]) for _ in range(len(heights))]
        visiteda=[[False]*len(heights[0]) for _ in range(len(heights))]
        for h in range(len(heights[0])):
            qp.append((0,h))
            visitedp[0][h]=True
        for h in range(1,len(heights)):
            qp.append((h,0))
            visitedp[h][0]=True
        for h in range(len(heights[0])):
            qa.append((len(heights)-1,h))
            visiteda[len(heights)-1][h]=True
        for h in range(0,len(heights)):
            qa.append((h,len(heights[0])-1))
            visiteda[h][len(heights[0])-1]=True
        
        while qp:
            n=len(qp)
            for _ in range(n):
                r,c=qp.popleft()
            
                if r+1<len(heights) and heights[r+1][c]>=heights[r][c] and not visitedp[r+1][c]:
                    qp.append((r+1,c))
                    visitedp[r+1][c]=True
                if r-1>=0 and heights[r-1][c]>=heights[r][c] and not visitedp[r-1][c]:
                    qp.append((r-1,c))
                    visitedp[r-1][c]=True
                if c+1<len(heights[0]) and heights[r][c+1]>=heights[r][c] and not visitedp[r][c+1]:
                    qp.append((r,c+1))
                    visitedp[r][c+1]=True
                if c-1>=0 and heights[r][c-1]>=heights[r][c] and not visitedp[r][c-1]:
                    qp.append((r,c-1))
                    visitedp[r][c-1]=True

        while qa:
            n=len(qa)
            for _ in range(n):
                r,c=qa.popleft()
            
                if r+1<len(heights) and heights[r+1][c]>=heights[r][c] and not visiteda[r+1][c]:
                    qa.append((r+1,c))
                    visiteda[r+1][c]=True
                if r-1>=0 and heights[r-1][c]>=heights[r][c] and not visiteda[r-1][c]:
                    qa.append((r-1,c))
                    visiteda[r-1][c]=True
                if c+1<len(heights[0]) and heights[r][c+1]>=heights[r][c] and not visiteda[r][c+1]:
                    qa.append((r,c+1))
                    visiteda[r][c+1]=True
                if c-1>=0 and heights[r][c-1]>=heights[r][c] and not visiteda[r][c-1]:
                    qa.append((r,c-1))
                    visiteda[r][c-1]=True

        res=[]
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if visiteda[r][c] and visitedp[r][c]:
                    res.append([r,c])
        return res

            


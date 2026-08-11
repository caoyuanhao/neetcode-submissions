class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent=list(range(len(points)))
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        dist=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                cost=abs(x1-x2)+abs(y1-y2)
                dist.append((cost,i,j))
        dist.sort()
        count=0
        res=0
        for cost,x,y in dist:
            px=find(x)
            py=find(y)
            if px!=py:
                parent[px]=py
                res+=cost
                count+=1
            
            if count==len(points)-1:
                return res
        return res
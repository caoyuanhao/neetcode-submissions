class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for x,y in points:
            dist=x**2+y**2
            heapq.heappush(h,(dist,x,y))
        res=[]
        for _ in range(k):
            _,x,y=heapq.heappop(h)
            res.append([x,y])
        return res



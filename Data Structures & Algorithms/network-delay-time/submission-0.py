import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float("inf")]*(n+1)
        h=[(0,k)]
        dist[k]=0

        while h:
            d,node=heapq.heappop(h)
            if d>dist[node]:
                continue
            
            for nei,weight in graph[node]:
                newDist=d+weight

                if newDist<dist[nei]:
                    dist[nei]=newDist
                    heapq.heappush(h,(newDist,nei))
        return -1 if float("inf") in dist[1:] else max(dist[1:])

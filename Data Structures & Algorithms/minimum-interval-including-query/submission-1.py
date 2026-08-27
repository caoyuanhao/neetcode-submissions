class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res=[-1]*len(queries)
        intervals.sort()
        q=[(queries[i],i) for i in range(len(queries))]
        q.sort()
        heap=[]
        j=0
        for i in q:           
            while j<len(intervals) and intervals[j][0]<=i[0]:
                heapq.heappush(heap,(intervals[j][1]-intervals[j][0]+1,intervals[j][1]))
                j+=1
            while heap and heap[0][1]<i[0]:
                heapq.heappop(heap)
            if heap:
                res[i[1]]=heap[0][0]
        return res
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        seq=sorted(tasks,key=lambda x:(x[0],x[1]))
        h=[]
        curr=0
        res=[]
        p=0
        while len(seq)>len(res):
            while p<len(seq) and seq[p][0]<=curr:
                heapq.heappush(h,[seq[p][1],seq[p][2]])
                p+=1
            if not h:
                curr=seq[p][0]
            else:
                time,i=heapq.heappop(h)
                res.append(i)
                curr+=time
        return res 
            
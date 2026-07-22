class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cou=Counter(tasks)
        h=list(cou.values())
        h=[-x for x in h]
        heapq.heapify(h)
        res=0
        full=True
        while h:
            temp=[]
            for i in range(n+1):
                if h:
                    c=-heapq.heappop(h)
                    if c>1:
                        temp.append(-(c-1))
                else:
                    full=False
                    break
            for x in temp:
                heapq.heappush(h,x)
            if h or full:
                res+=n+1
            else:
                res+=i
            

        return res
            
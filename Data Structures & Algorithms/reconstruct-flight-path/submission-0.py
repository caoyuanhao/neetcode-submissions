class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res=[]
        graph={}
        for u,v in tickets:
            if u not in graph:
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
        for c in graph:
            graph[c].sort(reverse=True)

        def dfs(city):
            while graph[city]:
                nextCity=graph[city].pop()
                dfs(nextCity)
            res.append(city)
        dfs("JFK")
        res.reverse()
        return res
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=0
        graph={i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for n in graph[node]:
                dfs(n)
            return 1

        for i in range(n):
            res+=dfs(i)
        return res
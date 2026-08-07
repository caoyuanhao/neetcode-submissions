class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        
        def dfs(node,parent):
            if node in visited:
                return False

            visited.add(node)
            for n in graph[node]:
                if n==parent:
                    continue
                if not dfs(n,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited)==n





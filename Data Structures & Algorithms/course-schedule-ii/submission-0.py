class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        visited=set()
        visiting=set()
        graph={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[v].append(u)

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res[::-1]
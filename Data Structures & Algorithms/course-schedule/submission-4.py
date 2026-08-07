class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[v].append(u)
        visited=set()
        visiting=set()

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

            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        

            

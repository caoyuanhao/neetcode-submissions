class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=list(range(len(edges)+1))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=parent[x],parent[y]
            if parent[x]==parent[y]:
                return False
            
            return True
        for e in edges:
            x,y=e[0],e[1]
            px=find(x)
            py=find(y)
            if px==py:
                return [x,y]
            parent[px]=py
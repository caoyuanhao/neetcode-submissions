class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(start,n,k,path):
            if len(path)==k:
                res.append(path.copy())
                return
            
            for i in range(start,n+1):
                if i not in path and len(path)<k:
                    path.append(i)
                    if start<n+1:    
                        backtrack(i+1,n,k,path)
                    path.pop()
        backtrack(1,n,k,[])
        return res
            
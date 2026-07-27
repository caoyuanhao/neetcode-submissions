class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       res=[]

       def backtrack(path,left,right):
        
        if right==n and left==n:
            temp="".join(path)
            res.append(temp)
            return 


        if left<n:
            path.append("(")
            backtrack(path,left+1,right)
            path.pop()
        if left>right:
            path.append(")")
            backtrack(path,left,right+1)
            path.pop()

        
       backtrack([],0,0)
       return res

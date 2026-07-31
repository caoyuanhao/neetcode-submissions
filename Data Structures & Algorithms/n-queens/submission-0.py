class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(row,col,path):
            i=1
            while row-i>=0:
                if path[row-i][col]=="Q":
                    return False
                i+=1
            i=1
            while col-i>=0 and row-i>=0:
                if path[row-i][col-i]=="Q":
                    return False
                i+=1
            i=1
            while col+i<n and row-i>=0:
                if path[row-i][col+i]=="Q":
                    return False
                i+=1
            return True
        res=[]
        path=[["."]*n for _ in range(n)]
        def backtrack(row):
            if row==n:
                temp=[]
                for i in range(n):
                    
                    temp.append("".join(path[i]))
                res.append(temp.copy())
                return

            for col in range(n):
                if isValid(row,col,path):
                    path[row][col]="Q"
                    backtrack(row+1)
                    path[row][col]="."

        backtrack(0)
        return res



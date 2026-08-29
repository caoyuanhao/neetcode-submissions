class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        zero=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero.append((i,j))
        for z in zero:
            for i in range(m):
                matrix[i][z[1]]=0
            for j in range(n):
                matrix[z[0]][j]=0

        
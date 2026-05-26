class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_c,right_c=0,len(matrix)-1
        left_r,right_r=0,len(matrix[0])-1
        while left_c<=right_c:
            mid_c=int((left_c+right_c)/2)
            if matrix[mid_c][0]<target:
                left_c=mid_c+1
            elif matrix[mid_c][0]>target:
                right_c=mid_c-1
            elif matrix[mid_c][0]==target:
                return True
        l=len(matrix)
        for i in range(len(matrix)):
            if target<matrix[i][0]:
                l=min(l,i)
        while left_r<=right_r:
            mid_r=int((left_r+right_r)/2)
            if matrix[l-1][mid_r]<target:
                left_r=mid_r+1
            elif matrix[l-1][mid_r]>target:
                right_r=mid_r-1
            elif matrix[l-1][mid_r]==target:
                return True           
        return False
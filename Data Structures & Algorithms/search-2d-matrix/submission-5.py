class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,column=len(matrix),len(matrix[0])
        left,right=0,row*column-1
        while left<=right:
            mid=int((left+right)/2)
            val=matrix[mid//column][mid%column]
            if val<target:
                left=mid+1
            elif val>target:
                right=mid-1
            elif val==target:
                return True
        return False
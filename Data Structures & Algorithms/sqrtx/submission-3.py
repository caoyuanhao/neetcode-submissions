class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        res=x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1
            elif mid*mid<x:
                res=mid
                left=mid+1

        return res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        res=1
        
        while n>=2:
            if n%2!=0:
                res*=x
                n=n-1
            x*=x
            n=n//2
        return res*x

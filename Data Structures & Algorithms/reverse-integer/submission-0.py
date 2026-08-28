class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if x<0:
            flag=-1
        else:
            flag=1
        res=0
        x=abs(x)
        while x:
            digit=x%10
            res=res*10+digit
            x=x//10
        if res*flag>2**31-1 or res*flag<-2**31:
            return 0
        return res*flag
            
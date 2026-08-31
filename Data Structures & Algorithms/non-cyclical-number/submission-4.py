class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            res=0
            while n:
                res+=(n%10)**2
                n=n//10
            return res
        slow=n
        fast=next_num(n)
        while slow!=fast:
            slow=next_num(slow)
            fast=next_num(next_num(fast))
        return slow==1
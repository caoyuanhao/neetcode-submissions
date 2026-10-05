class Solution:
    def tribonacci(self, n: int) -> int:
        l=[0,1,1]
        if n<3:
            return l[n]
        
        for i in range(n-3):
            l[i%3]=sum(l)
        return sum(l)
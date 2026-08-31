class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums=set()

        while n not in nums: 
            nums.add(n)
            res=0
            while n:
                res+=(n%10)**2
                n=n//10
            if res==1:
                return True
            else:
                
                n=res
        return False
        


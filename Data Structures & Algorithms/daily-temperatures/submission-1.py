class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for x in range(len(temperatures)):
            while stack and temperatures[x]>temperatures[stack[-1]]:
                i=stack.pop()
                res[i]=(x-i)
            
            stack.append(x)
        return res
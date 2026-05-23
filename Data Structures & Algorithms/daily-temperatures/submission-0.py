class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(len(temperatures)):
            d=0
            for j in range (i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    d=j-i
                    break
            res.append(d)
        return res
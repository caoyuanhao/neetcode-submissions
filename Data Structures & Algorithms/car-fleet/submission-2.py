class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=sorted(zip(position,speed),reverse=True)
        res=[]
        for p,v in s:
            t=(target-p)/v
            if not res or t>res[-1]:
                res.append(t)
        return len(res)
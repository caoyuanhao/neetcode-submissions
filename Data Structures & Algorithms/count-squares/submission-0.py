class CountSquares:

    def __init__(self):
        self.points={}

    def add(self, point: List[int]) -> None:
        p=(point[0],point[1])
        if p not in self.points:
            self.points[p]=1
        else:
            self.points[p]+=1

    def count(self, point: List[int]) -> int:
        x,y=point    
        res=0
        for (x2,y2) in self.points:
            if abs(x2-x)==abs(y2-y) and x!=x2 and y!=y2:
                nums=self.points.get((x2,y),0)*self.points.get((x,y2),0)*self.points.get((x2,y2),0)
                res+=nums
        return res

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        if len(asteroids)<=1:
            return asteroids
        res.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if res:
                left=res.pop()
                right=asteroids[i]
                if left>0 and right<0:
                    while left>0 and right<0:
                        if abs(left)>abs(right):
                            right=0
                            res.append(left)
                        elif abs(left)<abs(right):
                            if res:
                                left=res.pop()
                                if left<0 and right<0:
                                    res.append(left)
                                    res.append(right)
                            else:
                                res.append(right)
                                left=0
                        elif abs(left)==abs(right):
                            left=0
                            right=0
                else:
                    res.append(left)
                    res.append(right)
            else:
                res.append(asteroids[i])
        return res
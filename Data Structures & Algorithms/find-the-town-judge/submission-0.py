class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        relationship=[[0,0] for _ in range(n)]
        for r in trust:
            relationship[r[0]-1][0]+=1
            relationship[r[1]-1][1]+=1
        for i,r in enumerate(relationship):
            if r[0]==0 and r[1]==n-1:
                return i+1
        return -1
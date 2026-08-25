class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        m=[0]*len(target)
        for i in range(len(triplets)):
            flag=True
            for j in range(len(triplets[0])):
                if target[j]<triplets[i][j]:
                    flag=False
            if flag:
                for j in range(len(triplets[0])):
                    m[j]=max(m[j],triplets[i][j])
        return m==target


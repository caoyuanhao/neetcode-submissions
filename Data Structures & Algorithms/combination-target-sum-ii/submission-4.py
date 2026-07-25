class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates=sorted(candidates)
        def backtrack(start,path):
            cur_sum=sum(path)

            if cur_sum==target:
                res.append(path.copy())
                return
            if cur_sum>target:
                return
            
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res
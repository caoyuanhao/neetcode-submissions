class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def backtrack(start,path):
            if sum(path)==target:
                res.append(path.copy())
                return

            for i in range(start,len(nums)): 
                if sum(path)>target:
                    break               
                path.append(nums[i])
                backtrack(i,path)
                path.pop()
                
                
        

        backtrack(0,[])
        return res
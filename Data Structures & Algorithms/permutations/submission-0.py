class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtrack(path,used):
            if len(path)==len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]==False:
                    path.append(nums[i])
                    used[i]=True
                else:
                    continue
                backtrack(path,used)
                path.pop()
                used[i]=False
        backtrack([],[False]*len(nums))
        return res

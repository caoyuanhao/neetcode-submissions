class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        
        for i in range(len(nums)):
            if(dic.get(nums[i])!=i):
                flag=True
        
        return flag
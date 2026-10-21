class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        temp1=nums[len(nums)-k:len(nums)+1]
        t1=0
        temp2=nums[0:len(nums)-k]
        t2=0
        for i in range(len(nums)):
            if i<k:
                nums[i]=temp1[t1]
                t1+=1
            else:
                nums[i]=temp2[t2]
                t2+=1

        
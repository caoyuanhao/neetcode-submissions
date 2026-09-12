class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums,left,right):
            if left>=right:
                return
            mid=(left+right)//2
            pivot=nums[mid]
            l=left
            r=right
            while left<=right:
                while left<=r and nums[left]<pivot:
                    left+=1
                while right>=l and nums[right]>pivot:
                    right-=1
                if left<=right:
                    temp=nums[left]
                    nums[left]=nums[right]
                    nums[right]=temp
                    left+=1
                    right-=1
                
            quickSort(nums,left,r)
            quickSort(nums,l,right)
        quickSort(nums,0,len(nums)-1)
        return nums

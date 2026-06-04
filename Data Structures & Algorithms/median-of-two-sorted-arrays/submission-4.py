class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left,right=0,len(nums1)
        while left<=right:
            i=(left+right)//2
            j=(len(nums1)+len(nums2))//2-i
            n1_left  = nums1[i-1] if i > 0 else float('-inf')
            n1_right = nums1[i]   if i < len(nums1) else float('inf')
            n2_left  = nums2[j-1] if j > 0 else float('-inf')
            n2_right = nums2[j]   if j < len(nums2) else float('inf')
            if n1_left<=n2_right and n2_left<=n1_right:
                if(len(nums1)+len(nums2))%2==1:
                    return min(n1_right,n2_right)
                else:
                    return ((min(n1_right,n2_right)+max(n1_left,n2_left)))/2
            elif n1_right<=n2_left:
                left=i+1
            elif n1_left>n2_right:
                right=i-1

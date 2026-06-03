class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的数组，减少二分范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2   # nums1 左边取 i 个
            j = half - i              # nums2 左边取 j 个

            # 左右边界值（处理越界情况）
            nums1_left  = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i]   if i < m else float('inf')
            nums2_left  = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j]   if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 找到正确切割点
                if (m + n) % 2 == 1:
                    return float(min(nums1_right, nums2_right))
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1   # nums1 取多了，往左
            else:
                left = i + 1    # nums1 取少了，往右

        return -1
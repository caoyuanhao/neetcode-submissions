class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        while left<right:
            mid=int((left+right)/2)
            hours=sum(math.ceil(x/mid) for x in piles)
            if hours<=h:
                right=mid
            elif hours>h:
                left=mid+1
        return left


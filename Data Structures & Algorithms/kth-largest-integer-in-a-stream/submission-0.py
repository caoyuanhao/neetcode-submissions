from _heapq import heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.h=sorted(nums)[-k:]

        heapq.heapify(self.h)
    

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if len(self.h)>self.k:
            heapq.heappop(self.h)
        return self.h[0]

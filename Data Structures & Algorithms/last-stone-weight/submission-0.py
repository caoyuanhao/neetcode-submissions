class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:

            fir=-heapq.heappop(stones)
            sec=-heapq.heappop(stones)
            res=-abs(fir-sec)
            heapq.heappush(stones,res)
        return -heapq.heappop(stones)
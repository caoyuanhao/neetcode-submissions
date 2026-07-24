class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
        heapq.heapify(self.left)
        heapq.heapify(self.right)


    def addNum(self, num: int) -> None:
        if self.left and num>-self.left[0]:
            heapq.heappush(self.right,num)
        else:    
            heapq.heappush(self.left,-num)
        while len(self.left)>len(self.right)+1:
            temp=-heapq.heappop(self.left)
            heapq.heappush(self.right,temp)
        while len(self.right)>len(self.left):
            temp=-heapq.heappop(self.right)
            heapq.heappush(self.left,temp)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2
        
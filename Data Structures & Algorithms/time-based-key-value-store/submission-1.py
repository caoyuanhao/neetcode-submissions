class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        l=self.map[key]
        left=0
        right=len(l)-1
        res=""
        while left<=right:
            mid=(left+right)//2
            if l[mid][0]<=timestamp:
                res=l[mid][1]
                left=mid+1
            elif l[mid][0]>timestamp:
                right=mid-1
        return res

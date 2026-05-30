class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        pairs = self.map[key]
        # 二分找最后一个 timestamp <= 给定时间
        left, right = 0, len(pairs) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]  # 记录当前结果，继续往右找更大的
                left = mid + 1
            else:
                right = mid - 1
        return res
                

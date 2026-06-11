class LRUCache:

    def __init__(self, capacity: int):
        self.dict={}
        self.size=capacity
        self.queue=deque()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            while len(self.queue)>self.size:
                self.queue.popleft()
            return self.dict[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.queue.remove(key)
        self.dict[key]=value
        self.queue.append(key)
        if len(self.dict)>self.size:
            self.dict.pop(self.queue.popleft(),None)

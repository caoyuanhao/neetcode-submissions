class MyHashMap:

    def __init__(self):
        self.array=[[] for _ in range(10)]

    def put(self, key: int, value: int) -> None:
        index=key%10
        
        for d in self.array[index]:
            if d[0]==key:
                d[1]=value
                return

        self.array[index].append([key,value])

    def get(self, key: int) -> int:
        index=key%10
        if not self.array[index]:
            return -1
        for d in self.array[index]:
            if d[0]==key:
                return d[1]
        return -1

    def remove(self, key: int) -> None:
        index=key%10
        for d in self.array[index]:
            if d[0]==key:
                self.array[index].remove(d)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
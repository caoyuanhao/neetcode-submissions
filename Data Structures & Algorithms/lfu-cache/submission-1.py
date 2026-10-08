class LFUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cache_len=capacity
        self.curr=0
        self.record=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache[key][1]+=1
            times=self.cache[key][1]
            del self.record[times-1][key]
            self.record.setdefault(times,OrderedDict())[key]=1
            if times-1==self.curr and len(self.record[times-1])==0:
                self.curr+=1
            return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cache_len==0: 
            return
        if key in self.cache:
            self.cache[key][0]=value
            self.cache[key][1]+=1
            times=self.cache[key][1]
            del self.record[times-1][key]
            self.record.setdefault(times,OrderedDict())[key]=1
            if times-1==self.curr and len(self.record[times-1])==0:
                self.curr+=1
        else:
            if len(self.cache)<self.cache_len:
                self.cache.setdefault(key,[value,1])
                times=self.cache[key][1]
                self.record.setdefault(times,OrderedDict())[key]=1
                self.curr=times
            else:
                k,_=self.record[self.curr].popitem(last=False)
                del self.cache[k]
                self.cache.setdefault(key,[value,1])
                times=self.cache[key][1]
                self.record.setdefault(times,OrderedDict())[key]=1
                self.curr=times


            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
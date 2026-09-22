class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        if not self.q1 and not self.q2:
            self.q1.append(x)
        elif self.q1:
            self.q1.append(x)
        elif self.q2:
            self.q2.append(x) 

    def pop(self) -> int:
        if self.q1:
            while len(self.q1)!=1:
                self.q2.append(self.q1[0])
                del self.q1[0]
            res=self.q1[0]
            del self.q1[0]
            return res
        elif self.q2:
            while len(self.q2)!=1:
                self.q1.append(self.q2[0])
                del self.q2[0]
            res=self.q2[0]
            del self.q2[0]
            return res
        

    def top(self) -> int:
        if self.q1:
            while len(self.q1)!=1:
                self.q2.append(self.q1[0])
                del self.q1[0]
            res=self.q1[0]
            self.q2.append(res)
            del self.q1[0]
            return res
        elif self.q2:
            while len(self.q2)!=1:
                self.q1.append(self.q2[0])
                del self.q2[0]
            res=self.q2[0]
            self.q1.append(res)
            del self.q2[0]
            return res
        

    def empty(self) -> bool:
        return len(self.q1)==0 and len(self.q2)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
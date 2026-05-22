class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x=="(" or x=="[" or x=="{":
                stack.append(x)
            if stack==[]:
                return False
            if x==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(x)
            if x=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append(x)                    
            if x=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(x)
        if stack==[]:
            return True
        else:
            return False
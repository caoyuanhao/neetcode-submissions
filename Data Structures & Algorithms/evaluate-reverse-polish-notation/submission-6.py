import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv}
        stack=[]
        for x in tokens:
            if x in ops:
                b,a=stack.pop(),stack.pop()
                stack.append(int(ops[x](a,b)))
            else:
                stack.append(int(x))
        return stack[0]
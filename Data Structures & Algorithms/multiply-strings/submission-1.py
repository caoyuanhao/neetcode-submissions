class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_int(num):
            n=0
            for c in num:
                digit=ord(c)-ord("0")
                n=n*10+digit
            return n

        return str(to_int(num1)*to_int(num2))
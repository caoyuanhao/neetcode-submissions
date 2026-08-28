class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=0xFFFFFFFF
        while b!=0:
            s=(a^b)&MASK
            carry=((a&b)<<1)&MASK
            a=s
            b=carry
        if a > 0x7FFFFFFF:
            a -= 0x100000000
        return a
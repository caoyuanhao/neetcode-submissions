class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        i=0
        l=float("inf")
        for s in strs:
            l=min(len(s),l)
        while i<l:
            temp=strs[0][i]
            for s in strs:
                if temp!=s[i]:
                    return res
            res+=temp
            i+=1
        return res
                
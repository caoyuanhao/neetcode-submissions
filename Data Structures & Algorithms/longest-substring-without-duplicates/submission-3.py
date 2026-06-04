class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        res=0
        while right<len(s):
            while s[right] in s[left:right]:
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res

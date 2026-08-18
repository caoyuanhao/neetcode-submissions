class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                res+=1
                left-=1
                right+=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                left=i-1
                right=i
                while left>=0 and right<len(s) and s[left]==s[right]:
                    res+=1
                    left-=1
                    right+=1
                

        return res
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def ifPalindrome(s):
            left=0
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def backtrack(start,path):
            if len(s)==start:
                res.append(path.copy())
                return
            
            for i in range(start,len(s)):

                if ifPalindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return res
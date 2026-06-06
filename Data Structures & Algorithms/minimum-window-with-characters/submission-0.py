class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        left=0
        count_t={}
        window={}
        res=""
        for x in t:
            count_t[x]=count_t.get(x,0)+1

        have,total=0,len(count_t)
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            if s[right] in count_t and window[s[right]]==count_t[s[right]]:
                have+=1
            while have==total:
                if right-left+1<len(res) or not res:
                    res=s[left:right+1]
                window[s[left]]-=1
                if s[left] in count_t and count_t[s[left]]>window[s[left]]:
                    have-=1
                left+=1
        return res
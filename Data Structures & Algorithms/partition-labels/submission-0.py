class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last={}

        for i in range(len(s)):
            if s[i] not in last:
                last[s[i]]=i
            else:
                last[s[i]]=max(i,last[s[i]])

        res=[]
        start=0
        end=0

        for i in range(len(s)):
            end=max(last[s[i]],end)

            if i==end:
                res.append(end-start+1)
                start=i+1
        
        return res
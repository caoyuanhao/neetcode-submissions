class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        count1={}
        count2={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            count1[i]=count1.get(i,0)+1
        for i in range(left,left+len(s1)):
            count2[s2[i]]=count2.get(s2[i],0)+1
        for left in range(len(s2)-len(s1)+1):
            if count2==count1:
                return True
            count2[s2[left]]-=1
            if count2[s2[left]]==0:
                del count2[s2[left]]
            if left+len(s1)<len(s2):
                count2[s2[left+len(s1)]]=count2.get(s2[left+len(s1)],0)+1
            
        return False
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes={5:0,10:0,20:0}
        if bills[0]!=5:
            return False
        for bill in bills:
            if bill==5:
                changes[5]+=1
            elif bill==10:
                if changes[5]>0:
                    changes[5]-=1
                    changes[10]+=1
                else:
                    return False
            elif bill==20:
                if changes[10]>0 and changes[5]>0:
                    changes[10]-=1
                    changes[5]-=1
                    changes[20]+=1
                elif changes[5]>=3:
                    changes[5]-=3
                    changes[20]+=1
                else:
                    return False
        return True


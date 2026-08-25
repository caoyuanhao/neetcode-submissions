class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        count=Counter(hand)
        
        for start in hand:
            if count[start]==0:
                continue
            for i in range(groupSize):
                if count[start+i]==0:
                    return False
                count[start+i]-=1
        return True
        
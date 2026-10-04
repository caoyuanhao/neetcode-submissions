class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dist={}
        for i,c in enumerate(order):
            dist[c]=i
        l=len(words)
        for i in range(1,l):
            j=0
            left=words[i-1]
            right=words[i]
            ll=len(left)
            lr=len(right)
            while j<ll and j<lr:
                if dist[left[j]]>dist[right[j]]:
                    return False
                elif dist[left[j]]<dist[right[j]]:
                    break
                j+=1
            if j==lr and j<ll:
                return False
        return True

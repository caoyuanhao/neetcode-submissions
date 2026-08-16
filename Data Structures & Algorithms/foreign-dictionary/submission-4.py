class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph={c:set() for word in words for c in word}
        indegrees={c:0 for c in graph}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            s=True
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    s=False
                    if w2[j] not in graph[w1[j]]:    
                        graph[w1[j]].add(w2[j])
                        indegrees[w2[j]]+=1
                    break
            if s and len(w1)>len(w2):
                return ""
        queue=deque()
        for c in indegrees:
            if indegrees[c]==0:
                queue.append(c)
        res=""
        while queue:
            node=queue.popleft()
            for c in graph[node]:
                indegrees[c]-=1
                if indegrees[c]==0:
                    queue.append(c)
            res+=node
        if len(res)==len(indegrees):
            return res
        return ""

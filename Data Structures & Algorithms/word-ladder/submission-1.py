class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res=1
        queue=deque()
        queue.append(beginWord)
        word_set=set(wordList)
        if endWord not in word_set:
            return 0
        
        while queue:
            for _ in range(len(queue)):

                word=queue.popleft()
                if word==endWord:
                    return res

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word=word[:i]+c+word[i+1:]
                        if new_word in word_set:
                            queue.append(new_word)
                            word_set.remove(new_word)
                        
            res+=1
        return 0
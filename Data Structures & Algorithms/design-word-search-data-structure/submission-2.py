class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root

        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.isEnd=True
            
        

    def search(self, word: str) -> bool:
        node=self.root

        def backtrack(index,node):
            if index==len(word):
                return node.isEnd
            

            if word[index]==".":
                for child in node.children.values():
                    if backtrack(index+1,child)==True:
                        return True
                return False
                    

            elif word[index] in node.children:
                return backtrack(index+1,node.children[word[index]])

            
            else:
                return False
        
        res=backtrack(0,node)
        return res
        

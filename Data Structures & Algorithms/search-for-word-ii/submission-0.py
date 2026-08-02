class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]

        root=TrieNode()
        

        def insert(word):
            node=root
            for c in word:
                if c not in node.children:
                    node.children[c]=TrieNode()
                
                node=node.children[c]
            node.word=word  
            

        for w in words:
            insert(w)   


        visited=[[False]*len(board[0]) for _ in range(len(board))]          


        def backtrack(row,col,node):
            if row>=len(board) or col>=len(board[0]) or row<0 or col<0 or visited[row][col]==True:
                return

            if board[row][col] not in node.children:
                return 

            visited[row][col]=True
            node=node.children[board[row][col]]
            
            if node.word:
                res.append(node.word)
                node.word=None

                
            
            
            backtrack(row+1,col,node)
            backtrack(row-1,col,node)
            backtrack(row,col+1,node)
            backtrack(row,col-1,node)

            visited[row][col]=False
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r,c,root)
        return res


                    
            

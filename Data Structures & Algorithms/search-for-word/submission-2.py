class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited=[[False]*col for _ in range(row)]

        def backtrack(row,col,index):
        
            if row>=len(board) or col>=len(board[0]) or row<0 or col<0:
                return False
            
            if board[row][col]==word[index] and index==len(word)-1 and visited[row][col]==False:
                return True
            
            
            if board[row][col]==word[index] and visited[row][col]==False:
                visited[row][col]=True
                if backtrack(row+1,col,index+1):
                    return True
                if backtrack(row,col+1,index+1):
                    return True
                if backtrack(row-1,col,index+1):
                    return True
                if backtrack(row,col-1,index+1):
                    return True
                
                visited[row][col]=False
            
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
                    break
        return False

            
                


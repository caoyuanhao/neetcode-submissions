class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        arrived=[[False]*len(board[0]) for _ in range(len(board))]
        for r in range(len(board)):
            if board[r][0]=="O":
                q.append((r,0))
                arrived[r][0]=True
            if board[r][len(board[0])-1]=="O":
                q.append((r,len(board[0])-1))
                arrived[r][len(board[0])-1]=True
        for c in range(len(board[0])):
            if board[0][c]=="O":
                q.append((0,c))
                arrived[0][c]=True
            if board[len(board)-1][c]=="O":
                q.append((len(board)-1,c))
                arrived[len(board)-1][c]=True
        while q:
            r,c=q.popleft()
            if r-1>=0 and board[r-1][c]=="O" and not arrived[r-1][c]:
                q.append((r-1,c))
                arrived[r-1][c]=True
            if r+1<len(board) and board[r+1][c]=="O" and not arrived[r+1][c]:
                q.append((r+1,c))
                arrived[r+1][c]=True
            if c-1>=0 and board[r][c-1]=="O" and not arrived[r][c-1]:
                q.append((r,c-1))
                arrived[r][c-1]=True
            if c+1<len(board[0]) and board[r][c+1]=="O" and not arrived[r][c+1]:
                q.append((r,c+1))
                arrived[r][c+1]=True
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O" and not arrived[r][c]:
                    board[r][c]="X"
            

        

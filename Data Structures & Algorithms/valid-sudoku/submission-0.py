class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums=["1","2","3","4","5","6","7","8","9"]
        for i in range(9):
            row=[x for x in board[i] if x!="."]
            if len(row)!=len(set(row)):
                return False
            column=[board[r][i] for r in range(9) if board[r][i]!="."]
            if len(column)!=len(set(column)):
                return False
        for i in range(3):
            for j in range(3):
                box = [
                    board[r][c]
                    for r in range(i*3, i*3+3)
                    for c in range(j*3, j*3+3)
                    if board[r][c] != "."
                ]
                if len(box) != len(set(box)):
                    return False
        
        return True
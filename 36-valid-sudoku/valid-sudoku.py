class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                
                if(board[i][j]!="." and int(board[i][j])>0 and self.f(i,j,board)==False):
                    return False
        return True

    def f(self,i,j,board):
        for k in range(i+1,9):
            if board[k][j]==board[i][j]:
                return False

        for k in range(j+1,9):
            if board[i][k]==board[i][j]:
                return False
        sr=3*(i//3)
        sc=3*(j//3)
        for m in range(sr,sr+3):
            for n in range(sc,sc+3):
                if (m!=i and n!=j) and board[m][n]==board[i][j]:
                    return False
        

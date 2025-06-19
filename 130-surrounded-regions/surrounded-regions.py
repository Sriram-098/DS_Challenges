class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis=[[0]*len(board[0]) for _ in range(len(board))]

        def dfs(i,j,board,vis):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=="X" or vis[i][j]==1:
                return 

            vis[i][j]=1
            dfs(i-1,j,board,vis)
            dfs(i+1,j,board,vis)
            dfs(i,j-1,board,vis)
            dfs(i,j+1,board,vis)

        for i in range(len(board[0])):
            if board[0][i]=="O":
                dfs(0,i,board,vis)

        for i in range(len(board[0])):
            if board[len(board)-1][i]=="O":
                dfs(len(board)-1,i,board,vis)
   

        for i in range(len(board)):
            if board[i][0]=="O":
                dfs(i,0,board,vis)

        for i in range(len(board)):
            if board[i][len(board[0])-1]=="O":
                dfs(i,len(board[0])-1,board,vis)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if vis[i][j]==0 and board[i][j]=="O":
                    board[i][j]="X"



        
        
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,vis,board,pos,word):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or vis[i][j]==1 or board[i][j]!=word[pos]:
                return False
            
            if pos==len(word)-1:
                return True

            vis[i][j]=1
            x=dfs(i+1,j,vis,board,pos+1,word)
            y=dfs(i,j+1,vis,board,pos+1,word)
            z=dfs(i-1,j,vis,board,pos+1,word)
            m=dfs(i,j-1,vis,board,pos+1,word)
            vis[i][j]=0
            return x or y or z or m

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                vis=[[0]*len(board[0]) for i in range(len(board))]
                if board[i][j]==word[0] :
                    if(dfs(i,j,vis,board,0,word)):
                        return True
        return False

        
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        surr=[[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count=0
                if i>0 and board[i-1][j]==1:
                    count+=1
                if j>0 and board[i][j-1]==1:
                    count+=1

                if i<len(board)-1 and board[i+1][j]==1:
                    count+=1
                if j<len(board[0])-1 and board[i][j+1]==1:
                    count+=1

                if i>0 and j>0 and board[i-1][j-1]==1:
                    count+=1

                if i<len(board)-1 and j<len(board[0])-1 and board[i+1][j+1]==1:
                    count+=1

                if i>0 and j<len(board[0])-1 and board[i-1][j+1]==1:
                    count+=1

                if i<len(board)-1 and j>0 and board[i+1][j-1]==1:
                    count+=1
                surr[i][j]=count

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1 and surr[i][j]<2:
                    board[i][j]=0

                if board[i][j]==1 and (surr[i][j]==2 or surr[i][j]==3):
                    board[i][j]=1
                
                if board[i][j]==1 and surr[i][j]>3:
                    board[i][j]=0

                if board[i][j]==0 and surr[i][j]==3:
                    board[i][j]=1






       
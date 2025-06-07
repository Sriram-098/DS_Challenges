class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        chess=[["."]*n for i in range(n)]

        def top(i,j,chess,n):
            while(i>=0):
                if chess[i][j]=='Q':
                    return False
                i-=1
            return True

        def left(i,j,chess,n):
            while(j>=0):
                if chess[i][j]=='Q':
                    return False
                j-=1
            return True

        def leftdia(i,j,chess,n):
            while (i>=0 and j>=0):
                if chess[i][j]=='Q':
                    return False
                i-=1
                j-=1
            return True

        def rightdia(i,j,chess,n):
            while(i>=0 and j<n):
                if chess[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        def backtrack(i,chess,n):
            if i==n:
                x=[]
                for k in range(len(chess)):
                    x.append("".join(chess[k]))
                ans.append(x)
            
                return 


            for j in range(n):
                if top(i,j,chess,n) and left(i,j,chess,n) and leftdia(i,j,chess,n) and rightdia(i,j,chess,n):
                    chess[i][j]='Q'
                    backtrack(i+1,chess,n)
                    chess[i][j]='.'
        






        backtrack(0,chess,n)
        print(ans)
        return ans



       
                                                                                                                                      
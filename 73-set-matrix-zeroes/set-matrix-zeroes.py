class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q=deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    q.append([i,j])

        for i in range(len(q)):
            x,y=q.pop()
            self.f(x,y,matrix)
    
    def f(self,i,j,matrix):
        print(i,j)
        for k in range(0,len(matrix[0])):
            
            matrix[i][k]=0
        
        for k in range(0,len(matrix)):
            
            matrix[k][j]=0
        
        
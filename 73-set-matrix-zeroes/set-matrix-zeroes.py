class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        q=deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    q.append((i,j))

        while len(q)>0:
            m,n=q.popleft()
            for i in range(len(matrix[0])):
                matrix[m][i]=0
            for j in range(len(matrix)):
                matrix[j][n]=0

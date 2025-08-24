class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans=0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    ans+=matrix[i][j]
        print(matrix)
        for i in range(1,len(matrix)):
            ans+=matrix[i][0]
        for i in range(len(matrix[0])):
            ans+=matrix[0][i]
        return ans
        
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            for j in range(len(matrix[0])):
                matrix[i][j],matrix[len(matrix)-i-1][j]=matrix[len(matrix)-i-1][j],matrix[i][j]
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
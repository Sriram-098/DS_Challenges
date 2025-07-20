class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]  

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            val = matrix[i][j]
            length = 1
            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > val:
                    length = max(length, 1 + dfs(ni, nj))
            dp[i][j] = length
            return length

        maxi = 0
        for i in range(rows):
            for j in range(cols):
                maxi = max(maxi, dfs(i, j))

        return maxi

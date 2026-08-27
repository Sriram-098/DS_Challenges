class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[1e9]*(m+1) for _ in range(n+1)]
        dp[n-1][m-1]=grid[n-1][m-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    continue
                
                dp[i][j]=grid[i][j]+min(dp[i][j+1],dp[i+1][j])
        print(dp)
        return dp[0][0]
        
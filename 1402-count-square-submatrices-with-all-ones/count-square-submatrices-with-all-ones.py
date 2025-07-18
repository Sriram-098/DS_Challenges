class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        dp=[[0]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        for i in range(1,len(grid)+1):
            for j in range(1,len(grid[0])+1):
                if grid[i-1][j-1]==0:
                    continue
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])

        sq=0
        for i in range(len(grid)+1):
            for j in range(len(grid[0])+1):
                sq+=dp[i][j]

        return sq

        
        
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[-1]*len(grid[0]) for _ in range(len(grid))]
        
        def f(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 1e9
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            left=grid[i][j]+f(i-1,j)
            top=grid[i][j]+f(i,j-1)
            dp[i][j]=min(left,top)
            return dp[i][j]

        return f(len(grid)-1,len(grid[0])-1)
        
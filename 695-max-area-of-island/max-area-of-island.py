class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        ans=0

        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or vis[i][j]==1:
                return 0
            vis[i][j]=1
            return 1+dfs(i-1,j)+dfs(i+1,j) +dfs(i,j-1) +dfs(i,j+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j]==0 or grid[i][j]==1:
                    ans=max(dfs(i,j),ans)

        return ans
        
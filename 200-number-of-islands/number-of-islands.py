class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis=[[0]*len(grid[0]) for i in range(len(grid))]
        
        count=0

        def dfs(i,j,vis,grid):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or vis[i][j]==1 or grid[i][j]=="0":
                return

            vis[i][j]=1
            dfs(i+1,j,vis,grid)
            dfs(i-1,j,vis,grid)
            dfs(i,j+1,vis,grid)
            dfs(i,j-1,vis,grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j]==0 and grid[i][j]=="1":
                    count+=1
                    dfs(i,j,vis,grid)

        return count

        
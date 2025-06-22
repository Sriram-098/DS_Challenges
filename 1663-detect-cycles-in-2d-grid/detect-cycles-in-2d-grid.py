class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(r,c,pr,pc,vis,ch):
            if vis[r][c]==1:
                return True


            vis[r][c]=1
            dirs=((0,-1),(1,0),(0,1),(-1,0))
            for i,j in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    if grid[nr][nc]==ch and (nr!=pr or nc!=pc):
                        if dfs(nr,nc,r,c,vis,ch):
                            return True
            return False
            




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j]==0:
                    if(dfs(i,j,-1,-1,vis,grid[i][j])):
                        return True

        return False
        
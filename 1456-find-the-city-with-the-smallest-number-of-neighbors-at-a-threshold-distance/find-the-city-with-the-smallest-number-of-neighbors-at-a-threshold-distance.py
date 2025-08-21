class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        grid=[[1e9]*n for _ in range(n)]
        for u,v,wt in edges:
            grid[u][v]=wt
            grid[v][u]=wt
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j:
                        grid[i][j]=1e9
                    else:
                        grid[i][j]=min(grid[i][j],grid[i][k]+grid[k][j])
        ans=[0]*n
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<=distanceThreshold:
                    ans[i]+=1
        
        maxi=1e9
        print(ans)
        ind=-1
        for i in range(len(ans)):
            if ans[i]<=maxi:
                maxi=ans[i]
                ind=i

        return ind

        
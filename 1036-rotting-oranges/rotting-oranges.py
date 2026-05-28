class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        fresh =0
        q=deque()
        time=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        dirs=((0,-1),(1,0),(0,1),(-1,0))
        while q:
            qsi=len(q)
            for i in range(qsi):
                r,c=q.popleft()
                for j in range(len(dirs)):
                    nr=r+dirs[j][0]
                    nc=c+dirs[j][1]
                
                    if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]==1 and vis[nr][nc]==0:
                        fresh-=1
                        vis[nr][nc]=1
                        q.append((nr,nc))
                        grid[nr][nc]=2

            if q:
                time+=1
        if fresh ==0:
            return time
        else:
            return -1
            
            
        
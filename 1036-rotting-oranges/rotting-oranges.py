class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        dirs=((-1,0),(0,1),(1,0),(0,-1))
        time=0
        while q:
            qsize=len(q)
            for i in range(qsize):
                r,c=q.popleft()
                for i in range(len(dirs)):
                    nr=r+dirs[i][0]
                    nc=c+dirs[i][1]
                    if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]==1 and  vis[nr][nc]==0:
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        vis[nr][nc]=1
            if q:
                time+=1

        if fresh==0:
            return time
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        vis=set()
        q=deque()
        q.append((0,0,0,0))
        vis.add((0,0,0))
        dirs=((0,1),(1,0),(0,-1),(-1,0))
        while q:
            r,c,steps,obs=q.popleft()
            if r==len(grid)-1 and c==len(grid[0])-1:
                return steps
            for i in dirs:
                nr=r+i[0]
                nc=c+i[1]
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    newobs=obs+grid[nr][nc]
                    if newobs<=k and (nr,nc,newobs) not in vis:
                        q.append((nr,nc,steps+1,newobs))
                        vis.add((nr,nc,newobs))
        return -1


        
        

        
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        mat=[[1e9]*len(grid[0]) for _ in range(len(grid))]
        mat[0][0]=grid[0][0]
        q=deque()
        q.append((0,0))
        dirs=((-1,0),(0,1),(1,0),(0,-1))
        while q:
            r,c=q.popleft()
            for i in range(len(dirs)):
                nr=r+dirs[i][0]
                nc=c+dirs[i][1]
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    if mat[r][c]+grid[nr][nc]<mat[nr][nc]:
                        mat[nr][nc]=mat[r][c]+grid[nr][nc]
                        q.append((nr,nc))
        print(mat)
        return True if health-mat[len(grid)-1][len(grid[0])-1]>=1 else False

        
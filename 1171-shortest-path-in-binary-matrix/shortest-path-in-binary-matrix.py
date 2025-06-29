class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1

        mat=[[1e9]*len(grid[0]) for _ in range(len(grid))]
        mat[0][0]=1
        q=deque()
        q.append((0,0))
        dirs=((0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1))
        while q:
            r,c=q.popleft()
            for i,j in dirs:
                nr=r+i
                nc=c+j
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0 and mat[r][c]+1<mat[nr][nc]:
                    mat[nr][nc]=1+mat[r][c]
                    q.append((nr,nc))
        return mat[len(grid)-1][len(grid[0])-1] if mat[len(grid)-1][len(grid[0])-1]!=1e9 else -1


        
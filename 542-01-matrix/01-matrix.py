class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        vis=[[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j))
                    vis[i][j]=1
                    
        
        dirs=((0,-1),(-1,0),(0,1),(1,0))
        while q:
            r,c=q.popleft()
            for i in range(len(dirs)):
                nr=r+dirs[i][0]
                nc=c+dirs[i][1]
                if nr>=0 and nc>=0 and nr<len(mat) and nc <len(mat[0]) and vis[nr][nc]==0 and mat[nr][nc]>0:
                    
                    mat[nr][nc]=1+mat[r][c]
                    vis[nr][nc]=1
                    q.append((nr,nc))

        return mat

        
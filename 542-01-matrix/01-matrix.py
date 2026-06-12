class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        vis=[[0]*(len(mat[0])) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j))
                    vis[i][j]=1
        dirs=((0,1),(1,0),(-1,0),(0,-1))
        while len(q)>0:
            i,j=q.popleft()
            for r,c in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and mat[nr][nc]>0 and vis[nr][nc]==0:
                    mat[nr][nc]=1+mat[i][j]
                    vis[nr][nc]=1
                    q.append((nr,nc))
        return mat
        
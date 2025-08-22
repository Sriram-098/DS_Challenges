from queue import PriorityQueue
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        ls=[]
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1:
                    ls.append([forest[i][j],i,j])
        ls.sort()
        def bfs(sr,sc,er,ec):
            if sr==er and sc==ec:
                return 0
            q=deque()
            q.append((sr,sc,0))
            dirs=((-1,0),(0,1),(1,0),(0,-1))
            vis=[[0]*len(forest[0]) for _ in range(len(forest))]
            vis[sr][sc]=1
            while q:
                i,j,d=q.popleft()
                for r,c in dirs:
                    nr=r+i
                    nc=c+j
                    if 0<=nr<len(forest) and 0<=nc<len(forest[0]) and vis[nr][nc]==0 and forest[nr][nc]!=0:
                        if nr==er and nc==ec:
                            return d+1
                        vis[nr][nc]=1
                        q.append((nr,nc,d+1))
            return -1





        sr,sc=0,0
        ans=0
        for _ ,er,ec in ls:
            dist=bfs(sr,sc,er,ec)
            if dist==-1:
                return -1
            ans+=dist
            sr,sc=er,ec
        return ans


        


        
        
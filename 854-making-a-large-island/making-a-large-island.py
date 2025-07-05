class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.size=[1]*n
        
    
    def findultpar(self,u):
        if self.parent[u]==u:
            return self.parent[u]
            
        ulp=self.findultpar(self.parent[u])
        self.parent[u]=ulp
        return self.parent[u]
        
    def union(self,u,v):
        par_u=self.findultpar(u)
        par_v=self.findultpar(v)
        if par_u==par_v:
            return
        if self.rank[par_u]<self.rank[par_v]:
            self.parent[par_u]=par_v
        
        elif self.rank[par_u]>self.rank[par_v]:
            self.parent[par_v]=par_u
        else:
            self.parent[par_v]=par_u
            self.rank[par_u]+=1

    def unionsize(self,u,v):
        par_u=self.findultpar(u)
        par_v=self.findultpar(v)
        if par_u==par_v:
            return 
        if self.size[par_u]<self.size[par_v]:
            self.parent[par_u]=par_v
            self.size[par_v]+=self.size[par_u]

        else:
            
            self.parent[par_v]=par_u
            self.size[par_u]+=self.size[par_v]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ds=DisjointSet(len(grid)*len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dirs=((-1,0),(0,1),(1,0),(0,-1))
                    for r,c in dirs:
                        nr=i+r
                        nc=j+c
                        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                            currnode=i*len(grid[0])+j
                            adjnode=nr*len(grid[0])+nc
                            ds.unionsize(currnode,adjnode)
        
        maxi=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s=set()
                if grid[i][j]==0:
                    dirs=((-1,0),(0,1),(1,0),(0,-1))
                    for r,c in dirs:
                        nr=i+r
                        nc=j+c

                        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                            s.add(ds.findultpar(nr*len(grid[0])+nc))
                x=0
                for k in s:
                    x+=ds.size[k]
                maxi=max(maxi,x+1)

        for i in range(len(grid)*len(grid[0])):
            maxi=max(maxi,ds.size[ds.findultpar(i)])
        return  maxi

                            


                        

        


        
class Disjointset:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        
    def findultpar(self,u):
        if self.parent[u]==u:
            return self.parent[u]
            
        ulp=self.findultpar(self.parent[u])
        self.parent[u]=ulp
        return self.parent[u]
        
    def union(self,u,v):
        par_u=self.findultpar(u)
        par_v=self.findultpar(v)
        if par_u ==par_v:
            return 
        if self.rank[par_u] <self.rank[par_v]:
            self.parent[par_u]=par_v
            
        elif self.rank[par_u]>self.rank[par_v]:
            self.parent[par_v]=par_u
        else:
            self.parent[par_v]=par_u
            
            self.rank[par_u]+=1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds=Disjointset(len(edges)+1)
        ans=[0,0]
        for u,v in edges:
            if ds.findultpar(u)!=ds.findultpar(v):
                ds.union(u,v)
            else:
                ans=[u,v]
        return ans
        
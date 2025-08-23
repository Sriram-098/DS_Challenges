class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    def findpar(self,u):
        if self.parent[u]==u:
            return self.parent[u]
        ulp=self.findpar(self.parent[u])
        self.parent[u]=ulp
        return self.parent[u]
    def findrank(self,u,v):
        par_u=self.parent[u]
        par_v=self.parent[v]
        if par_u ==par_v:
            return 
        if self.rank[par_u]>self.rank[par_v]:
            self.parent[par_v]=par_u
        elif self.rank[par_v]>self.rank[par_u]:
            self.parent[par_u]=par_v
        else:
            self.rank[par_u]+=1
            self.parent[par_v]=par_u

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds=DisjointSet(len(edges))
        ans=[]
        for u,v in edges:
            if ds.findpar(u)!=ds.findpar(v):
                ds.findrank(u,v)
            else:
                ans.append([u,v])
        return ans[len(ans)-1]
        
class Disjointset():
    def __init__(self,n):
        self.par=[i for i in range(n+1)]
        self.rank=[0]*(n+1)

    def findpar(self,u):
        if self.par[u]==u:
            return self.par[u]

        ulp=self.findpar(self.par[u])
        self.par[u]=ulp
        return self.par[u]

    def findrank(self,u,v):
        par_u=self.findpar(u)
        par_v=self.findpar(v)

        if par_u==par_v:
            return 

        if self.rank[par_u]>self.rank[par_v]:
            self.par[par_v]=par_u

        elif self.rank[par_v]>self.rank[par_u]:
            self.par[par_u]=par_v

        else:
            self.rank[par_u]+=1
            self.par[par_v]=par_u

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds=Disjointset(len(edges))
        ans=[]
        for u,v in edges:
            if ds.findpar(u)!=ds.findpar(v):
                ds.findrank(u,v)
            else:
                ans.append([u,v])
        return ans[len(ans)-1]
        
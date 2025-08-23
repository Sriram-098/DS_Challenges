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
        par_u=self.findpar(u)
        par_v=self.findpar(v)
        if par_u ==par_v:
            return False
        if self.rank[par_u]>self.rank[par_v]:
            self.parent[par_v]=par_u
        elif self.rank[par_v]>self.rank[par_u]:
            self.parent[par_u]=par_v
        else:
            self.rank[par_u]+=1
            self.parent[par_v]=par_u
        return True
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        ds=DisjointSet(len(edges))
        par=[0]*(len(edges)+1)
        cand1=[]
        cand2=[]
        for u,v in edges:
            if par[v]==0:
                par[v]=u
            else:
                cand1=[par[v],v]
                cand2=[u,v]
                break
        for u,v in edges:
            if [u,v] == cand2:
                continue
            if not ds.findrank(u,v):
                if cand1:
                    return cand1
                return [u,v]
        return cand2




        
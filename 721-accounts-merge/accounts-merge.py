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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds=Disjointset(len(accounts))
        m={}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in m:
                    m[accounts[i][j]]=i
                else:
                    ds.union(m.get(accounts[i][j]),i)
        ls=[[] for _ in range(len(accounts))]
        
        for key,val in m.items():
            par=ds.findultpar(val)
            ls[par].append(key)
        
        for i in range(len(ls)):
            ls[i]=sorted(ls[i])

        ans=[]
        for i in range(len(accounts)):
            if ls[i]:
                print(accounts[i][0],ls[i])
                temp=[accounts[i][0]]+ls[i]
                ans.append(temp)
        return ans
        
        
       
            




        
mod=10**9+7
from queue import PriorityQueue
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        count=[0]*n
        adj=[[] for _ in range(n)]
        for u,v,wt in roads:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
            
        q=PriorityQueue()
        q.put((0,0))
        dis=[float('inf')]*n
        dis[0]=0
        count[0]=1
        while not q.empty():
            d,node=q.get()
            if d>dis[node]:
                continue
            for nei,wt in adj[node]:
                if wt+d<dis[nei]:
                    dis[nei]=d+wt
                    count[nei]=count[node]
                    q.put((dis[nei],nei))
                elif wt+d==dis[nei]:
                    count[nei]=(count[node]+count[nei])%mod
        print(count)
        return count[n-1]

        
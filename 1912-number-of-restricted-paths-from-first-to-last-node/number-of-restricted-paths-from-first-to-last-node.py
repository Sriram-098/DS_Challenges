from queue import PriorityQueue
from collections import deque
from functools import lru_cache
mod=10**9+7
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        
        dis=[float('inf')]*(n+1)
        dis[n]=0
        pq=PriorityQueue()
        pq.put((0,n))
        while not pq.empty():
            d,node=pq.get()
            for nei,wt in adj[node]:
                if d+wt<dis[nei]:
                    
                    dis[nei]=d+wt
                    pq.put((dis[nei],nei))
        print(dis)
        @lru_cache(None)
        def dfs(i):
            if i==n:
                return 1
            total=0
            for nei,wt in adj[i]:
                if dis[i]>dis[nei]:
                    total+=dfs(nei)
                
            return total%mod
        return dfs(1)

    
        
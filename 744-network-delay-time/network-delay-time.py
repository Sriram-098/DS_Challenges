from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        q=PriorityQueue()
        q.put((0,k))
        vis=[False]*(n+1)
        vis[k]=True
        vis[0]=True
        d={}
        while not q.empty():
            t,node=q.get()
            vis[node]=True
            if node in d:
                continue
            if node not in d:
                d[node]=t
            for nei,wt in adj[node]:
                    q.put((t+wt,nei))
                    
        print(vis,d)
        return max(d.values()) if all(vis) else -1
        
        
        
    



        
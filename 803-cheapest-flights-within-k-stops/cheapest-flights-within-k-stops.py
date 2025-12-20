from queue import PriorityQueue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,wt in flights:
            adj[u].append([v,wt])
        
        pq=PriorityQueue()
        pq.put((0,0,src))
        dis=[1e9]*n
        dis[src]=0
        while pq.qsize()>0:
            stops,effort,node=pq.get()
            if stops >k:
                continue
            for nei,wt in adj[node]:
                if wt+effort<dis[nei]:
                    dis[nei]=wt+effort

                    pq.put((stops+1,dis[nei],nei))

        return dis[dst] if dis[dst]!=1e9 else -1

       
        


        

        
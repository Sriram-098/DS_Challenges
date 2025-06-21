from queue import PriorityQueue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        
        for u,v,charge in flights:
            adj[u].append((v,charge))
        print(adj)
        pq=PriorityQueue()
        pq.put((0,0,src))
        ans=[1e9]*n
        ans[src]=0
        while not pq.empty():
            
            limit,charge,currstop=pq.get()
            if limit>k:
                continue
            for i in adj[currstop]:
                v=i[0]
                weight=i[1]
                if limit<=k and charge+weight<ans[v]:
                    ans[v]=charge+weight
                    pq.put((limit+1,ans[v],v))

        return ans[dst] if ans[dst]!=1e9 else -1

                    

            
        
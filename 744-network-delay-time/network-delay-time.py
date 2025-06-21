from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,time in times:
            adj[u].append((v,time))

        time=0
        pq=PriorityQueue()
        pq.put((0,k))
        s={}
        while not pq.empty():
            time,node=pq.get()
            if node in s:
                continue
            s[node]=time
            for nei,wt in adj[node]:
                if nei not in s:
                    
                    pq.put((time+wt,nei))
        return max(s.values()) if n==len(s) else -1
        
        
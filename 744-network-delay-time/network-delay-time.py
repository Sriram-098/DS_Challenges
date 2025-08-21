from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        q=PriorityQueue()
        q.put((0,k))
        time=[1e9]*(n+1)
        time[k]=0
        time[0]=0
        
        while not q.empty():
            t,node=q.get()
            for nei,wt in adj[node]:
                if wt+t<time[nei]:
                    q.put((wt+t,nei))
                    time[nei]=wt+t
        ans=0     
        print(time)
        for i in range(len(time)):
            if time[i]==1e9:
                return -1
            ans=max(ans,time[i])
        return ans

            
        
        
        
    



        
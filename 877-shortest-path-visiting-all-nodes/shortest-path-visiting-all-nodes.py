from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph)==1 and len(graph[0])==0:
            return 0
        finalstate=(1<<len(graph))-1
        q=deque()
        vis=[[0]*(finalstate+1) for _ in range(len(graph))]
        for i in range(len(graph)):
            q.append((i,1<<i))
            vis[i][i<<1]=1
        ans=0
        
        
        while q:
            s=len(q)
            ans+=1
            
            for _ in range(s):
                node,state=q.popleft()
                for nei in graph[node]:
                    newstate=state|1<<nei
                    if vis[nei][newstate]==1:
                        continue
                    vis[nei][newstate]=1
                    q.append((nei,newstate))
                    if newstate==finalstate:
                        return ans
        return ans

            
        
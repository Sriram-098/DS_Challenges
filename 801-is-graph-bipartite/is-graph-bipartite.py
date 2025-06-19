class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q=deque()
        
        color=[-1]*len(graph)
        
        vis=[0]*len(graph)
        vis[0]=1
        for j in range(len(graph)):
            if color[j]==-1:
                q.append(j)
                color[j]=0
                vis[j]=1
            while len(q)>0:
                node=q.popleft()
                
                
                for i in graph[node]:
                    if vis[i]==0:
                        vis[node]=1
                        
                        color[i]=1-color[node]
                        q.append(i)
                    elif color[i]==color[node]:
                        return False
        return True

        
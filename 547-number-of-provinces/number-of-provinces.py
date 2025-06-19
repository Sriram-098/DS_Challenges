class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=[[] for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    adj[i].append(j)
        
        def dfs(i,vis,adj):
            vis[i]=1
            for j in adj[i]:
                if vis[j]==0:
                    dfs(j,vis,adj)
        count=0
        vis=[0]*len(isConnected)
        for i in range(len(isConnected)):
            if vis[i]==0:
                count+=1
                dfs(i,vis,adj)

        return count
        
        
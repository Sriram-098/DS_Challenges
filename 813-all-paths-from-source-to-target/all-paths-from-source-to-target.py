class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        vis=[0]*len(graph)
        ans=[]
        def dfs(i,sub):
            if i==len(graph)-1:
                ans.append(sub.copy())
                return 

            for nei in graph[i]:
                if vis[nei]==0:
                    vis[nei]=1
                    sub.append(nei)
                    dfs(nei,sub)
                    sub.pop()
                    vis[nei]=0
        vis[0]=1
        dfs(0,[0])
        return ans

        
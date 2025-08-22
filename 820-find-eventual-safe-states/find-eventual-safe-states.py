class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis=[0]*len(graph)
        def dfs(i):
            if vis[i]==1:
                return False
            if vis[i]==2:
                return True
            vis[i]=1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            vis[i]=2
            return True


        ans=[]
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans
        
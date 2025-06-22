class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:




        vis=[0]*len(graph)
        def dfs(node):
            if vis[node]==1:
                return False
            if vis[node]==2:
                return True
            vis[node]=1



            for nei in graph[node]:
                if not dfs(nei):
                    return False
            

            vis[node]=2
            return True



        ans=[]
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans     

        
        
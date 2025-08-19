class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj=[[] for _ in range(n)]
        s=set(restricted)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis=[0]*n
        def dfs(i):
            vis[i]=1
            for nei in adj[i]:
                if vis[nei]==0 and nei not in s:
                    dfs(nei)
        dfs(0)

        return sum(vis)


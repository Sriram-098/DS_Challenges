class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=[0]*len(rooms)
        vis[0]=1
        def dfs(i):
            vis[i]=1
            for nei in rooms[i]:
                if vis[nei]==0:
                    dfs(nei)
        dfs(0)
        return all(vis)
        
        
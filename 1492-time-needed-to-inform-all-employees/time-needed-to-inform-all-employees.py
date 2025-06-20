class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj=[[]for _ in range(n)]
        for i in range(len(manager)):
            if manager[i]==-1:
                continue
            adj[manager[i]].append(i)
        
        q=deque()
        q.append((headID,0))
        print(q)
        maxtime=0
        while len(q)>0:
            print(q[0])
            curr_man,time_yet=q.popleft()
            maxtime=max(maxtime,time_yet)
            for subor in adj[curr_man]:
                q.append((subor,time_yet+informTime[curr_man]))
        return maxtime
        
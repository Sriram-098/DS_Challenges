class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        
        indre=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indre[j]+=1
        
        q=deque()
        for i in range(numCourses):
            if indre[i]==0:
                q.append(i)

        lis=[]
        while q:
            node=q.popleft()
            lis.append(node)
            for i in adj[node]:
                indre[i]-=1
                if indre[i]==0:
                    q.append(i)
        lis.reverse()
        return lis if len(lis)==numCourses else []
        
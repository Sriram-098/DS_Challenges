class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(len(colors))]
        for u,v in edges:
            adj[u].append((v))
        ind=[0]*(len(colors))
        dp=[[0]*26 for _ in range(len(colors))]

        for i in range(len(colors)):
            for j in adj[i]:
                ind[j]+=1
        q=deque()
        for i in range(len(colors)):
            if ind[i]==0:
                q.append(i)
        print(q)
        count=0
        ans=0
        while q:
            node=q.popleft()
            count+=1
            colind=ord(colors[node])-ord('a')
            dp[node][colind]+=1
            ans=max(ans,dp[node][colind])

            for nei in adj[node]:
                for i in range(26):
                    dp[nei][i]=max(dp[node][i], dp[nei][i])
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return ans if count==len(colors) else -1
        
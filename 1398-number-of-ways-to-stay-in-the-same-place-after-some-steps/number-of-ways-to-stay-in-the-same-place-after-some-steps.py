
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod=10**9+7
        pos=min(steps,arrLen-1)
        dp=[[-1]*(steps+1) for _ in range(pos+1)]
        
       
        def dfs(i,steps):
            if steps==0:
                return 1 if i==0 else 0
            if dp[i][steps]!=-1:
                return dp[i][steps]
            result=dfs(i,steps-1)
            if i>0:
                result=(result+dfs(i-1,steps-1))%mod
            if i<pos:
                result=(result+dfs(i+1,steps-1))%mod
            dp[i][steps]=result
            return dp[i][steps]

        return dfs(0,steps)
        
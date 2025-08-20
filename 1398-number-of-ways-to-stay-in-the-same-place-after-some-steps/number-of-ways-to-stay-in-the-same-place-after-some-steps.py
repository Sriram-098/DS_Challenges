from functools import lru_cache
MOD=10**9+7

class Solution:
    def numWays(self,steps, arrLen):
        maxPos = min(steps, arrLen-1)

        @lru_cache(None)
        def dfs(i, pos):
            if i == 0:
                return 1 if pos == 0 else 0
            ans = dfs(i-1, pos)  # stay
            if pos > 0:
                ans += dfs(i-1, pos-1)  # left
            if pos < maxPos:
                ans += dfs(i-1, pos+1)  # right
            return ans % MOD

        return dfs(steps, 0)


            

        



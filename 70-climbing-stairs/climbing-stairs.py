class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def help(i):
            if dp[i]:
                return dp[i]
            if i==0:
                return 1
            if i<0:
                return 0

            onestep=help(i-1)
            twostep=help(i-2)
            dp[i]=onestep+twostep
            return dp[i]


        return help(n)
        
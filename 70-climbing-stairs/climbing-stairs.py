class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def helper(n):
            if dp[n]!=-1:
                return dp[n]
            if n==0:
                return 1

            if n<0:
                return 0
            onestep=helper(n-1)
            twostep=helper(n-2)
            dp[n]=onestep+twostep
            return dp[n]

        return helper(n)
        
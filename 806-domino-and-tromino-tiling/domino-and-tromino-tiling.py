mod=10**9+7
class Solution:
    def numTilings(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(i):
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                return 1
            if i==1:
                return 1
            if i==2:
                return 2
            dp[i]=(2*f(i-1)+f(i-3))%mod
            return dp[i]



        return f(n)
        
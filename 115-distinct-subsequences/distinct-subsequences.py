class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1]*(len(t)+1) for _ in range(len(s)+1)]
        def f(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if j<0:
                return 1
            if i<0:
                return 0
            
            if s[i]==t[j]:
                dp[i][j]=f(i-1,j-1)+f(i-1,j)
                return dp[i][j]
            dp[i][j]=f(i-1,j)
            return dp[i][j]





        return f(len(s)-1,len(t)-1)
        
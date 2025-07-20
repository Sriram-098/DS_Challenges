class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1]*(len(s)+1)for _ in range(len(p)+1)]
        def f(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i<0 and j<0 :
                return True
            if i<0 and j>=0:
                return False
            if j<0 and i>=0 :
                for k in range(i+1):
                    if p[k]!='*':
                        return False
                return True

            if p[i]=='?'or p[i]==s[j]:
                dp[i][j]=f(i-1,j-1)
                return dp[i][j]

            if p[i]=='*':
                dp[i][j]=f(i-1,j) or  f(i,j-1)
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]

        return  f(len(p)-1,len(s)-1)
        
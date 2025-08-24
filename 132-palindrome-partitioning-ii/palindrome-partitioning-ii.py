class Solution:
    def minCut(self, s: str) -> int:
        dp=[-1]*(len(s)+1)
        def ispalindrome(x):
            return x==x[::-1]
        def check(start):
            if start==len(s):
                return 0
            if dp[start]!=-1:
                return dp[start]
            mincost=1e9
            for end in range(start,len(s)):
                if ispalindrome(s[start:end+1]):
                    mincost=min(mincost,1+check(end+1))
                    dp[start]=mincost
            return dp[start]




        return check(0)-1
        
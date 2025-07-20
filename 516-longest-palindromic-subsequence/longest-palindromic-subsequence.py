class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1=s
        text2=s[::-1]
        print(text2)
        dp=[[-1]*(len(text2)+1) for _ in range(len(text1)+1)]
        def f(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+f(i-1,j-1)
                return dp[i][j]
            dp[i][j]=max(f(i-1,j),f(i,j-1))
            return dp[i][j]



        return f(len(text1)-1,len(text2)-1)
        
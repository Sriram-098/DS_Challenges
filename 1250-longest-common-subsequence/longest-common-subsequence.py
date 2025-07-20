class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]'''
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
        
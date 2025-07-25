class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*len(word2) for _ in range(len(word1))]

        def f(i,j):

            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=f(i-1,j-1)
                return dp[i][j]
            
            insertion=1+f(i,j-1)
            deletion=1+f(i-1,j)
            replace=1+f(i-1,j-1)
            dp[i][j]=min(insertion,deletion,replace)
            return dp[i][j]



    
        return f(len(word1)-1,len(word2)-1)
        
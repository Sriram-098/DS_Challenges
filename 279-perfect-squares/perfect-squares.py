class Solution:
    def numSquares(self, n: int) -> int:
        if n==1:
            return 1
        sq=[]
        for i in range(1,int(n**0.5)+1):
            sq.append(i*i)
        #print(sq)

        dp=[[1e9]*(n+1) for _ in range(len(sq)+1)]
        for i in range(len(sq)+1):
            dp[i][0]=0

        for i in range(1,len(sq)+1):
            curr_ele=sq[i-1]
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]
                if curr_ele<=j:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-curr_ele])
        #print(dp)
        return dp[len(sq)][n]

        
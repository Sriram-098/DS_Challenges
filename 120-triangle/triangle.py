class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp=[[-1]*len(triangle[len(triangle)-1]) for _ in range(len(triangle))]
        def f(i,j):
            if i==len(triangle)-1:
                return triangle[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]


            st=triangle[i][j]+f(i+1,j)
            stdo=triangle[i][j]+f(i+1,j+1)
            dp[i][j]=min(st,stdo)
            return dp[i][j]

        return f(0,0)
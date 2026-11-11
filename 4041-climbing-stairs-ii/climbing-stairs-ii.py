class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[1e9]*n
        dp[0]=costs[0]+1
        if n>=2:
            dp[1]=min(dp[0]+costs[1]+1,costs[1]+4)
        if n>=3:
            dp[2]=min(costs[2]+9, dp[0]+costs[2]+4,dp[1]+costs[2]+1)

        for i in range(3, len(costs)):
            dp[i] = min(
                dp[i-1] + costs[i] + 1,
                dp[i-2] + costs[i] + 4,
                dp[i-3] + costs[i] + 9
    )

        print(dp)
        return dp[-1]


        
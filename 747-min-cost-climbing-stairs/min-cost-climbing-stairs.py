class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*len(cost)
        def f(i):
            if i==0:
                return cost[0]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            onestep=cost[i]+f(i-1)
            twostep=cost[i]+f(i-2)
            dp[i]=min(onestep,twostep)
            return dp[i]

        return min(f(len(cost)-1),f(len(cost)-2))
    
        
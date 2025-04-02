class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1]*2 for _ in range(len(prices)+1)]
        return self.f(0,1,prices,dp)
    
    def f(self,i,buy,prices,dp):
        if(i==len(prices)):
            return 0
        
        if(dp[i][buy]!=-1):
            return dp[i][buy]

        profit=0
        if(buy==1):
            profit=max(-prices[i]+self.f(i+1,0,prices,dp),self.f(i+1,1,prices,dp))
        else:
            profit=max(prices[i]+self.f(i+1,1,prices,dp),self.f(i+1,0,prices,dp))

        dp[i][buy]=profit
        return dp[i][buy]
        
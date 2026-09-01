class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[1e9]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=0

        for i in range(1,len(coins)+1):
            curr_ele=coins[i-1]
            for j in range(1,amount+1):
                dp[i][j]=dp[i-1][j]
                if curr_ele<=j:
                    dp[i][j]=min(dp[i-1][j], 1+ dp[i][j-curr_ele])
        return dp[len(coins)][amount] if dp[len(coins)][amount]!=1e9 else -1
        
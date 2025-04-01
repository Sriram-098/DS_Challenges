class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=1e9
        profit=0
        for i in range(len(prices)):
            mini=min(prices[i],mini)
            profit=max(profit,prices[i]-mini)
        return profit

        
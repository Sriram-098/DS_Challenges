class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=1e9
        for i in range(len(prices)):
            mini=min(prices[i],mini)
            maxi=max(maxi,prices[i]-mini)
        return maxi
        
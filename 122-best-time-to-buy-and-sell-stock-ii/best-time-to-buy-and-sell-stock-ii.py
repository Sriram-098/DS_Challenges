class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold=-prices[0]
        cash=0
        for i in range(len(prices)):
            prevhold=hold
            prevcash=cash
            hold=max(prevhold,prevcash-prices[i])
            cash=max(prevcash,prevhold+prices[i])
        return cash

        
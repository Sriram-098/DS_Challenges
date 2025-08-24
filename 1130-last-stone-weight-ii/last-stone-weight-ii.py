import math
from queue import PriorityQueue
class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        totalsum = sum(nums)
        half = math.ceil(totalsum / 2)   # integer floor division

        # dp[i][t] = None (uncomputed) or True/False whether we can make sum t using nums[0..i]
        dp = [[None] * (half + 1) for _ in range(n)]

        def f(i, target):
            if target == 0:
                return True
            if i == 0:
                return nums[0] == target
            if dp[i][target] is not None:
                return dp[i][target]

            not_pick = f(i - 1, target)
            pick = False
            if nums[i] <= target:
                pick = f(i - 1, target - nums[i])

            dp[i][target] = pick or not_pick
            return dp[i][target]

        # Ensure we compute for every target in [0..half]
        for t in range(half + 1):
            f(n - 1, t)

        mini = float('inf')
        for t in range(half + 1):
            if dp[n - 1][t]:
                mini = min(mini, abs(totalsum - 2*t))
        return mini
            
        
            

        
        
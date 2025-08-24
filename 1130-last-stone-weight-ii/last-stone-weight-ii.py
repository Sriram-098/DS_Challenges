import math
from queue import PriorityQueue

class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        half=ceil(totalsum/2)
        dp=[[None]*(half+1) for _ in range(len(nums))]
        def f(i,target):
            if target==0:
                return True
            if i==0:
                return target==nums[0]
            if dp[i][target]!=None:
                return dp[i][target]
            nonpick=f(i-1,target)
            pick=False
            if target>=nums[i]:
                pick=f(i-1,target-nums[i])
            dp[i][target]=pick or nonpick
            return dp[i][target]

        for t in range(half+1):
            f(len(nums)-1,t)
        #print(dp)
        best=0
        for i in range(half+1):
            if dp[len(nums)-1][i]:
                best=i
        return abs((totalsum-best)-best)
        
        
            

        
        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum=0
        for i in range(len(nums)):
            totalsum+=nums[i]
        if totalsum-target<0 or (totalsum-target)%2!=0:
            return 0
        totalsum=(totalsum-target)//2
        dp=[[-1]*(totalsum+1) for _ in range(len(nums))]
        def f(i,target):
            if i==0:
                if target==0 and nums[i]==0:
                    return 2
                elif target==nums[0] or target==0:
                    return 1
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            nonpick=f(i-1,target)
            pick=0
            if target>=nums[i]:
                pick=f(i-1,target-nums[i])
            dp[i][target]=pick + nonpick
            return dp[i][target]
        return f(len(nums)-1,totalsum)
        
        
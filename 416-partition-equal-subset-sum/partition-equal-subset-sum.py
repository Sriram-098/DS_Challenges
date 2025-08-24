class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=0
        for i in range(len(nums)):
            totalsum+=nums[i]
        if totalsum%2!=0:
            return False
        totalsum=totalsum//2
        dp=[[-1]*(totalsum+1) for _ in range(len(nums))]
        def f(i,target):
            if target==0:
                return True
            if i==0:
                return target==nums[0]
            if dp[i][target]!=-1:
                return dp[i][target]
            nonpick=f(i-1,target)
            pick=False
            if target>=nums[i]:
                pick=f(i-1,target-nums[i])
            dp[i][target]=pick or nonpick
            return dp[i][target]
        
        return f(len(nums)-1,totalsum)

        
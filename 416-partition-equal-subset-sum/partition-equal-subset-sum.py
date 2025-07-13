class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=sum(nums)
        if totalsum%2!=0:
            return False
        
        dp=[[-1]*((totalsum//2)+1) for i in range(len(nums))]

        

        def f(i,target):
            if i==0:
                return nums[i]==target
            if target==0:
                return True
            if dp[i][target]!=-1:
                return dp[i][target]

            nottake=f(i-1,target)
            take=False
            if target>=nums[i]:
                take=f(i-1,target-nums[i])
            dp[i][target]=take or nottake
            return dp[i][target]
                


        
        return f(len(nums)-1,totalsum//2)
    
        
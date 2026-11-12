class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        dp1=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=1+dp[i-1]
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                dp1[i]=1+dp1[i-1]
        print(dp,dp1)
        return max(max(dp),max(dp1))

        
            
        
        

        
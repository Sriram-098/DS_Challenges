class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums.sort()
        maxi=1
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                dp[i]=1+dp[i-1]
            elif nums[i-1]==nums[i]:
                dp[i]=dp[i-1]
            maxi=max(maxi,dp[i])
            

        return maxi
        
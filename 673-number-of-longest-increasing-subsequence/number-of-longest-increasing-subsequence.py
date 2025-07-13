class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        maxi=1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    count[i]=count[j]

                elif nums[i]>nums[j] and 1+dp[j]==dp[i]:
                    count[i]+=count[j]

                maxi=max(dp[i],maxi)
        ans=0
        for i in range(len(nums)):
            if dp[i]==maxi:
                ans+=count[i]

        return ans
        
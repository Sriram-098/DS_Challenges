class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[1]*len(nums)
        ind=[0]*len(nums)
        maxi=0
        maxind=0
        for i in range(len(nums)):
            ind[i]=i
            for j in range(i):
                if nums[i]%nums[j]==0 and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    ind[i]=j

            if dp[i]>maxi:
                maxi=dp[i]
                maxind=i
            
                    

        ans=[]
        ans.append(nums[maxind])
        while(maxind !=ind[maxind]):
            maxind=ind[maxind]
            ans.append(nums[maxind])

        return ans[::-1]
            
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def f(arr,i,dp):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick=arr[i]+f(arr,i-2,dp)
            nonpick=f(arr,i-1,dp)
            dp[i]=max(nonpick,pick)
            return dp[i]
        
        arr1=nums[0:len(nums)-1]
        arr2=nums[1:len(nums)]
        dp1=[-1]*len(arr1)
        dp2=[-1]*len(arr1)
        return max(f(arr1,len(arr1)-1,dp1),f(arr2,len(nums)-2,dp2))
        
        
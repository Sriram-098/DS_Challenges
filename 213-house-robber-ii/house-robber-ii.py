class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        frst =nums[0:n-1]
        second=nums[1:n]
        print(frst,second)
        def helper(arr):
            n=len(arr)
            dp=[0]*(n+2)
            for i in range(n-1,-1,-1):
                dp[i]=max(arr[i]+dp[i+2],dp[i+1])
            print(dp)
            return dp[0]
    
        return max(helper(frst),helper(second))
        
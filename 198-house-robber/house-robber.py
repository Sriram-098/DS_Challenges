class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        def robhouse(i):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]

            onehouse=nums[i]+robhouse(i-2)
            another=0+robhouse(i-1)
            dp[i]=max(onehouse,another)
            return dp[i]


        return robhouse(len(nums)-1)


        
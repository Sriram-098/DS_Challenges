class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        l=0
        r=0
        while(r<len(nums)):
            if nums[r]==0:
                l=r
                while(r<len(nums) and nums[r]==0 ):
                    ans+=(r-l+1)
                    r+=1
            else:
                r+=1
        return ans

        
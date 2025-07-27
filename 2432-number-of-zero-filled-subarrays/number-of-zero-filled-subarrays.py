class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        while(r<len(nums)):
            if(nums[r]==0):
                l=r

            while( r<len(nums) and nums[r]==0 ):
                count+=(r-l+1)
                r+=1
            r+=1

        return count
        
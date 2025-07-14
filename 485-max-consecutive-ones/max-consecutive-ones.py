class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        r=0
        maxi=0
        count=0
        while r<len(nums):
            if nums[r]==0:
                l=r+1
            
            
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi






        
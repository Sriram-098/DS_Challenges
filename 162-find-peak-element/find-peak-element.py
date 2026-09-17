class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l=1
        r=len(nums)-2
        if len(nums)>1 and nums[0]>nums[1]:
          
            return 0
        if len(nums)>1 and nums[len(nums)-2]<nums[len(nums)-1]:
            return len(nums)-1
        
        while l<=r:
            mid=(l+(r-l)//2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return 0  
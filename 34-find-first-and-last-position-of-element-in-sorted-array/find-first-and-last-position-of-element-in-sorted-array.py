class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        a=self.lower(nums,target)
        b=self.upper(nums,target)
        print(a,b)
        if a<len(nums) and b<len(nums) and (nums[a]!=target and nums[b]!=target) or len(nums)==0:
            return ans
        ans=[a,b]
        return ans

    def lower(self,nums,target):
        low=0
        high=len(nums)-1
        while(low<high):
            mid=int((low+high)/2)
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid

            

        return low

    def upper(self,nums,target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            
            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1

        return low-1
        
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=max(nums)
        while(low<=high):
            mid=(low+high)//2
            check=self.f(nums,mid,threshold)
            if check==True:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


    def f(self,nums,mid,threshold):
        rem=0
        for i in range(len(nums)):
            rem+=math.ceil(nums[i]/mid)
            if rem>threshold:
                return False
        return True
        
        
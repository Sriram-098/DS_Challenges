class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def f(x):
            count=0
            for i in range(len(nums)):
                count+=math.ceil(nums[i]/x)
            return count
                
        l=1
        r=max(nums)
        ans=0
        while l<=r:
            mid=(l+r)//2
            check=f(mid)
            if check<=threshold:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        
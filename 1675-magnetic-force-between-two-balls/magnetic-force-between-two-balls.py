class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def f(nums,mid,m):
            last=nums[0]
            count=0
            for i in range(1,len(nums)):
                if nums[i]-last>=mid:
                    last=nums[i]
                    count+=1
            count+=1

            return count>=m
            

        low=1
        high=sum(position)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            check=f(position,mid,m)
            if check:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        
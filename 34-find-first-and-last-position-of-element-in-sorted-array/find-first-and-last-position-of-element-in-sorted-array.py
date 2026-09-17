class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:


        ans=[-1,-1]
        def lower_bound():
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return l
        def upper_bound():
            l=0
            r=len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                
                if nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
            return l

        a=lower_bound()
        b=upper_bound()-1
        print(a,b)
        if a>=len(nums)  or nums[a]!=target or nums[b]!=target:
            return [-1,-1]
        return [a,b]

            
    
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        
        
        def lower():
            l=0
            r=len(nums)-1
            while l<r:
                mid=(l+r)//2
                if nums[mid]<target:  
                    l=mid+1
                else:
                    r=mid
            return l

        def upper():
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
            return l-1
        
        a=lower()
        b=upper()
        if a<0 or b<0 or a>=len(nums) or nums[a]!=target:
            return ans
        ans[0]=a
        ans[1]=b
        
        return ans

        


            
        
        
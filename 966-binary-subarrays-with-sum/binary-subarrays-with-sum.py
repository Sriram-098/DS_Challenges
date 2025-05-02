class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      
        return self.f(nums,goal)-self.f(nums,goal-1)



    def f(self,nums,k):

        l=0
        count=0
        s=0
        r=0
        while(r<len(nums)):
            s+=nums[r]
            while(l<r and s>k):
                s-=nums[l]
                l+=1
                
            
            if s<=k:
                
                count+=(r-l+1)
            

            r+=1

        return count


        
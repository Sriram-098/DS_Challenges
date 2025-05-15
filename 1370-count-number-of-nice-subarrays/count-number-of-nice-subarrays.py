class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        
        return self.f(nums,k)-self.f(nums,k-1)


    def f(self,nums,k):
        count=0
        l=0
        r=0
        s=0
        while(r<len(nums)):
            s+=nums[r]
            while(s>k):
                s-=nums[l]
                l+=1
            
            if s<=k:
                count+=(r-l+1)
            r+=1

        return count

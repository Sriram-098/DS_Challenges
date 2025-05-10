class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=0
        s=0
        l=0
        r=0
        maxi=-1e9
        while(r<len(nums)):
            s+=nums[r]
            while((r-l+1)>k):
                s-=nums[l]
                l+=1

            if (r-l+1)==k:
                maxi=max(s/k,maxi)
            
            r+=1
        return maxi

        
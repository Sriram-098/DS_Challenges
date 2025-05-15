class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        maxlen=0
        count=0
        while(r<len(nums)):
            if nums[r]==1:
                count+=1
            
            while((r-l+1)-count>k):
                if nums[l]==1:
                    count-=1
                l+=1
            
            if (r-l+1)-count <=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        
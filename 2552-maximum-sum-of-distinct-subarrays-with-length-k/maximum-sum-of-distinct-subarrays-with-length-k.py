class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        maxi=0
        s=0
        store=set()
        while(r<len(nums)):
            
            while nums[r] in store or ((r-l+1)>k):
                
                store.remove(nums[l])
                s-=nums[l]
                l+=1
            store.add(nums[r])
            s+=nums[r]
            if (r-l+1) ==k:
                maxi=max(s,maxi)
            r+=1
        return maxi
                
        
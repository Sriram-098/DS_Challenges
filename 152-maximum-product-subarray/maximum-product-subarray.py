class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxpro=-1e9
        pref=1
        suff=1
        for i in range(len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref=pref*nums[i]
            suff=suff*nums[len(nums)-i-1]
            maxpro=max(maxpro,max(pref,suff))
        return maxpro
            
            
        return maxpro
        
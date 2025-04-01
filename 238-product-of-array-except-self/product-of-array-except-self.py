class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        pref[0]=1
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]*nums[i-1]

        suff=1
        for i in range(len(nums)-1,-1,-1):
            pref[i]*=suff
            suff*=nums[i]
        return pref

        
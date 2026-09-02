class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=1
        mini=1
        ans=-1e9
        for i in range(len(nums)):
            if nums[i]<0:
                maxi,mini=mini,maxi
            
            maxi=max(nums[i],maxi*nums[i])
            mini=min(nums[i],mini*nums[i])
            ans=max(ans,maxi,mini)
        return ans

        
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        s=0
        ans=0
        se=set()
        while r<len(nums):
            s+=nums[r]
            

            while nums[r] in se or  r-l+1 >k :
                s-=nums[l]
                se.remove(nums[l])
                l+=1
            se.add(nums[r])
            if r-l+1 ==k:
                ans=max(ans,s)
            r+=1

        return ans 


        
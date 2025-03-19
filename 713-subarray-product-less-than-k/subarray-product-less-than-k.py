class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        count=0
        pro=1
        while(r<len(nums)):
            pro*=nums[r]

            while(pro>=k and l<=r):

                pro=pro//nums[l]
                l+=1
            
            if pro<k:
                
                count+=(r-l+1)
            r+=1
        return count

    

        
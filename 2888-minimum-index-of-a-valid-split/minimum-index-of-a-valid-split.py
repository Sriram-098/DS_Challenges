from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d2=Counter(nums)
        d1=dict()

        for i in range(len(nums)):
            d1[nums[i]]=d1.get(nums[i],0)+1

            d2[nums[i]]-=1

            if ((d2.get(nums[i])*2)>len(nums)-i-1  and d1[nums[i]]*2 > i+1):
                return i

        return -1
        


        
        
        
        
        
        